#!/usr/bin/env python3
"""District education indicators from the NISR Rwanda Population and Housing Census 2022 public-use file.
Source: NISR, microdata.statistics.gov.rw, study RWA-NISR-RPHC-2022-v0.1 (file PHC5_Public_microdata.dta).
Usage: python3 census_education.py PHC5_Public_microdata.dta        (needs: pip install pandas)
Output: district_education.csv  (aggregated only; raw microdata is NOT published)
The file is NISR's 10% equal-probability sample of private households (institutions excluded). Percentages are weighted with Pop_weight; the sample is self-weighting, so unweighted percentages are almost identical.
Age groups follow NISR's census education report (school age 6-17)."""
import os, sys, pandas as pd
cols = ['ml01','ml02','p03','p04','p29','p30a','p32','Pop_weight']
d = pd.read_stata(sys.argv[1], columns=cols, convert_categoricals=True)
d = d[d.p29.isin(['Has previously attended','Is currentely attending','Has never attended'])]   # drops 174 invalid codes
d['prov'], d['dist'], d['w'] = d.ml01.astype(str), d.ml02.astype(str), d.Pop_weight.astype(float)
def pct(x, g):                       # weighted % of group g where condition x is true
    return round(100 * (x[g].astype(float) * d.w[g]).sum() / d.w[g].sum(), 1)
kids = (d.p04 >= 6) & (d.p04 <= 17); adults = d.p04 >= 25; lit15 = (d.p04 >= 15) & d.p32.notna()
att = d.p29 == 'Is currentely attending'
upper = d.p30a.isin(['Lower secondary','Upper secondary','Tertiary'])      # missing p30a = never attended
literate = ~d.p32.astype(str).isin(['None','Not stated'])
rows = []
for name, g in d.groupby('dist'):
    i = g.index; k = kids & d.index.isin(i); f = d.p03 == 'Female'
    rows.append({'District': name, 'Province': g.prov.iloc[0], 'Children_6_17_est': int(round(d.w[k].sum(), -2)), 'Sample_children_6_17': int(k.sum()),
      'Attending_6_17_pct': pct(att, k), 'Girls_attending_pct': pct(att, k & f), 'Boys_attending_pct': pct(att, k & ~f),
      'Adults25plus_lower_secondary_or_higher_pct': pct(upper, adults & d.index.isin(i)),
      'Literate_15plus_pct': pct(literate, lit15 & d.index.isin(i))})
out = pd.DataFrame(rows).sort_values('District'); out.to_csv(sys.argv[2] if len(sys.argv) > 2 else 'district_education.csv', index=False)
print(out.to_string(index=False)); print('National 6-17 attending %:', pct(att, kids))

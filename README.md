# Edudata-rwanda: education data and library for Rwanda
By Manthedan (INES-Ruhengeri) · Manzi Brian Bonheur and Igihozo Narada · Contact: manzib301@gmail.com · 0796829887
Entry for the NISR 2026 Big Data Hackathon.

- **Live app:** https://manthedan26.github.io/Edudata-Rwanda/
- **Demo video (max 3 minutes):** [`demo/demo.webm`](demo/demo.webm) (also shown at the bottom of the Home tab)
- **Student cards (eligibility):** [`student_cards/student_cards.pdf`](student_cards/student_cards.pdf)

## Repository structure
| Path | What it is |
|---|---|
| `README.md` | this documentation |
| `index.html` | the whole website (HTML, CSS and JavaScript, the census results and the map in one file, so it runs on any machine and on GitHub Pages) |
| `census_education.py`, `requirements.txt` | Python script that rebuilds the district results from the NISR census file |
| `data/district_education.csv` | the data we use: Census 2022 district results (aggregated) |
| `demo/demo.webm` | screen recording of the platform |
| `student_cards/student_cards.pdf` | student cards of the two team members |
| `sw.js`, `ai-worker.js`, `LICENSE` | offline cache, optional online AI server code, licence note |

## What data it uses
| Data | Source | Where |
|---|---|---|
| **Census 2022 education indicators** by district (attendance ages 6-17, adult secondary education, literacy) | NISR, Rwanda Population and Housing Census 2022, public-use microdata (study RWA-NISR-RPHC-2022-v0.1), weighted with `Pop_weight` | `data/district_education.csv`. The raw microdata is not published: download it from https://microdata.statistics.gov.rw/index.php/catalog/109 |
| National school figures 2024/25 (schools, learners, owner, status, disability, internet, pupil/classroom) | MINEDUC Education Statistical Yearbook 2024/2025 | Overview and Insights tabs |
| District map background | NISR, Administrative map of Rwanda (c) NISR 2017 | Census tab |
| Textbooks and past papers (links only) | REB eLearning, NESA | Library tab |
| Method documents | NISR Census 2022 data dictionary, Statement of the Public Use Sample, thematic report "Educational characteristics of the population" | used to design and check the method |

## What it communicates
Where children go to school and where adults reach secondary education or read and write, district by district; official national school figures (owner, status, learners with disabilities); and one place to find official books and exam papers. Relevant to Vision 2050 and NST2 priorities on human capital and education.

## How users interact with it
Open the live link or `index.html`. Tabs: **Home** (platform, demo video), **Overview** (official indicators), **Library** (REB books, NESA past papers), **Census** (rank the 30 districts by an indicator, see them on the district map, download the CSV), **Insights** (schools by owner, status and learners with disabilities; download CSV or PDF), **Sources** (every source and the method), **About** (platforms, national priorities, declaration, feedback, contact). EN/FR/RW language selector, dark mode, and a chat assistant (bottom right) that answers questions about the platform in Kinyarwanda, English and French. A Feedback button opens a Google Form.

## Alignment with national priorities
Vision 2050 aims for upper-middle income by 2035 and high income by 2050. The second National Strategy for Transformation (NST2, 2024-2029) has three pillars (Economic Transformation, Social Transformation, Transformational Governance); education sits in the Social Transformation pillar, and one stated NST2 priority is improving the quality and market relevance of education. Edudata-rwanda supports this with (1) official REB books and NESA past papers in one place, (2) district-level evidence from NISR Census 2022 and MINEDUC figures, and (3) free digital access in Kinyarwanda, English and French. It supports these priorities; it is not an official NST2 monitoring tool and does not measure teaching quality.

## Method (Census tab)
`census_education.py` (needs `pip install -r requirements.txt`): keep valid attendance codes; attendance = currently attending, ages 6-17; adults = age 25+ with lower secondary, upper secondary or tertiary as highest level; literacy = reads and writes in at least one language, ages 15+; every percentage is weighted with the population weight.
Sample: NISR's public-use file is a 10% equal-probability sample of private households (institutions excluded); it is self-weighting, so weighted and unweighted percentages are almost identical.
Validation: our attendance for ages 6-11 (89.4%) and 12-17 (73.2%) and literacy 15+ (78.8%) match or nearly match NISR's published education thematic report (89.4%, 73.1%, 78.8%).
Limits: small district differences may not be meaningful; results are not official NISR statistics.
Reproduce: `python3 census_education.py PHC5_Public_microdata.dta` writes `data/district_education.csv`.

## Declaration of authorship and use of AI
This project is the work of Manzi Brian Bonheur and Igihozo Narada (team Manthedan, INES-Ruhengeri). We chose the topic and the goals, decided which features the platform needs, obtained the NISR Census 2022 data from the NISR microdata portal and the MINEDUC figures, reviewed and tested the platform on phones and computers, and set up the live website on GitHub Pages and the user feedback form.

We used an **AI assistant (Claude, by Anthropic)** as a helper. Following our instructions, it wrote **most of the program code** (HTML, CSS, JavaScript and Python) and the first drafts of the documentation and presentation. We reviewed, tested and corrected its work. We declare this openly, as the hackathon rules require, and we take responsibility for everything in this submission. NISR guidance: AI tools are allowed as assistants if declared.

## Credits
Census 2022 results and the administrative map: "Source: National Institute of Statistics of Rwanda (NISR)". School figures: MINEDUC Education Statistical Yearbook 2024/2025. Books and past papers: REB eLearning and NESA (links only).

# Steam Digital Gaming Ecosystem & Player Analytics

An interactive web-based data analytics application built with **Python**, **Streamlit**, and **Altair** to explore pricing strategies, catalog trends, and player engagement across 27,000+ titles in the Steam ecosystem.

---

## Overview

Developed as part of **MCA411-2 PYTHON Programming** (Regular Lab Exercise 6) at Department of Computer Science.
- **Author**: Denzil Deepak A (Reg. No: 2647216)
- **Class**: 1MCA-B
- **Faculty**: Prof. Kavitha R
- **Dataset**: `dataset/steam.csv` (27,075 titles across 18 attributes)

---

## Features & Layouts

- **Executive KPIs**: Real-time summary cards displaying Total Games, Average Price, Positive Review Ratio (%), and Free-to-Play ratio.
- **Interactive Sidebar Filters**:
  - Full-text search for game titles and publishers.
  - Multi-select filtering across primary genres.
  - Interactive price range slider ($0.00 – $400.00+).
  - Release year range slider (1997 – 2019).
  - Target operating system selector (Windows, macOS, Linux).
- **Analytical Visualizations (Altair)**:
  - **Bar Chart**: Top 10 primary genres by catalog game count.
  - **Line Chart**: Historical release trajectory illustrating the market expansion since 2014 (Steam Greenlight / Direct).
  - **Scatter Plot**: Price strategy vs. player satisfaction with point sizing mapped to review volume.
- **Catalog Explorer**: Searchable, paginated table view with instant one-click CSV data export.
- **Strategic Insights**: Collapsible sections detailing commercial viability, pricing ceilings, and storefront discovery algorithms.

---

## Quickstart (Local Run)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Denzils-repo/steam_analytics.git
   cd steam_analytics
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```
   Open your browser at `http://localhost:8501`.

---

## Project Structure

```text
steam_analytics/
│
├── .streamlit/
│   └── config.toml           # Steam dark theme configuration
│
├── dataset/
│   └── steam.csv             # Full Steam games dataset (27,075 records)
│
├── programs/
│   └── 2647216_P6.py         # Main Steam Analytics Streamlit application
│
├── .gitignore                # Git ignore patterns
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── streamlit_app.py          # Streamlit Community Cloud entry point
```

---

## Tech Stack

- **Python 3.10+**
- **Streamlit** (Web application framework & reactive layout engine)
- **Pandas** (Data wrangling & filtering)
- **Altair** (Declarative statistical data visualization)

# Codveda Data Analysis Internship

This repository contains my data analysis and preprocessing tasks completed during the **Codveda Technology** internship using Python and data science libraries.

## Repository Structure

- `Level_1/Task1_Data_Cleaning/` — Data cleaning and preprocessing on the Iris dataset (`task1_data_cleaning.py` and `final_iris.csv`).
- `Level_2/` — Intermediate tasks (to be added: at least 2 tasks).
- `Level_3/` — Advanced tasks (to be added: at least 2 tasks).

## Completed Tasks

### Level 1 — Basic

#### Task 1: Data Cleaning and Preprocessing (Iris Dataset)
- **What I did:**
  - Loaded the Iris dataset using `pandas`.
  - Checked for missing values (`isnull().sum()`) and removed incomplete rows with `dropna()`.
  - Checked for duplicate records (`duplicated()`) and removed duplicates with `drop_duplicates()`.
  - Standardized the `species` column (`astype(str).str.lower().str.strip()`).
  - Exported the cleaned dataset to `final_iris.csv` without the extra index column (`index=False`).
- **Tools & Libraries:** Python, Google Colab, `pandas`.

## Future Tasks
- Complete the second task in Level 1, followed by at least two tasks each in Level 2 and Level 3.

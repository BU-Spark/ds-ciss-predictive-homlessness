# Community-Level Homelessness Prediction Model

## Project Overview
This project develops a predictive model for homelessness at the community level, analyzing data from 2010–2023 across approximately 400 Continuums of Care (CoCs) funded by the U.S. Department of Housing and Urban Development (HUD). Unlike prior studies focusing on individual-level predictions, this project emphasizes structural factors such as rent levels, economic conditions, and unemployment rates to forecast homelessness rates or counts.

**Goal:** Provide actionable insights for policymakers and community organizations to optimize resource allocation and implement timely interventions to reduce homelessness.

## Objectives
- Identify and correct errors and inconsistencies in the dataset inherited from the previous semester's team
- Develop machine learning models with improved accuracy compared to previous semester's models

## Big Impact
By modeling community-level drivers of homelessness, this project enables:
- Efficient resource allocation for assistance programs
- Identification of key socioeconomic factors influencing homelessness trends
- Timely policy interventions to reduce homelessness on a larger scale

## Repository Structure


## Key Files
### Python Notebooks
1. **Fix_Rent_+_Income.ipynb**
   - **Purpose:** Processes American Community Survey (ACS) census tract data to correct errors in rent and income calculations
   - **Key Features:**
     - Downloads ACS data (population, rent, income) directly from U.S. Census Bureau
     - Computes population-weighted averages using:  
       `Weighted Average = Σ(Valueᵢ × Populationᵢ) / ΣPopulationᵢ`
     - Addresses previous inflation issues (e.g., mean rent ~$186K → corrected values)
   - **Output:** Generates `corrected_stuff.csv`

2. **Regression_w_fixed_targets.ipynb**
   - **Purpose:** Builds linear regression models with corrected data
   - **Key Features:**
     - Normalizes target variables per 1,000 people:  
       `Normalized Target = (Raw Count / Population) × 1,000`
     - Generates visualizations:
       - Feature correlation plots
       - Regression coefficient matrices

## Datasets
- **Primary Sources:**
  - [ACS Population Data (B01003)](https://www.census.gov/)
  - [ACS Rent Data (B25064)](https://www.census.gov/)
  - [ACS Income Data (B19013)](https://www.census.gov/)
- **Point-in-Time (PIT) Data:** Used for homelessness counts (merged with ACS data)

## Data Cleaning Highlights
| Issue | Fix |
|-------|-----|
| 42% missing bed data | Imputed zeros for missing values |
| Inflated rent/income values | Implemented population-weighted averages |
| Erroneous "total homeless" row | Removed outlier |
| Incorrect normalization | Standardized per 1,000 people |

## Model Development
### Approaches
1. **Linear Regression**
   - Baseline interpretable model
   - Improved with normalized targets
2. **Neural Network**
   - Captures nonlinear relationships
   - Features: L2 regularization, 20% dropout, early stopping
3. **XGBoost** *(In Progress)*

### All Models were run with our teams final dataset that has all the corrections described in final report: `CISS_final_df2.csv`

### Evaluation Metrics
- **MAE** (Mean Absolute Error)
- **R²** (Coefficient of Determination)

## Key Findings
- **Strongest Predictors:**
  - Renter Household Rate (~0.4 correlation)
  - Cost Burdened Rate (~0.3)
  - Unemployment Rate (~0.25)
- **Trends (2007-2023):**
  - Post-2020 surge in unsheltered homelessness
  - Family homelessness correlates with extreme socioeconomic conditions


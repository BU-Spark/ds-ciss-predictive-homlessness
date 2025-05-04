Community-Level Homelessness Prediction Model

Project Overview

This project develops a predictive model for homelessness at the community level, analyzing data from 2010–2023 across approximately 400 Continuums of Care (CoCs) funded by the U.S. Department of Housing and Urban Development (HUD). Unlike prior studies focusing on individual-level predictions, this project emphasizes structural factors such as rent levels, economic conditions, and unemployment rates to forecast homelessness rates or counts. The goal is to provide actionable insights for policymakers and community organizations to optimize resource allocation and implement timely interventions to reduce homelessness.

Objectives





Identify and correct errors and inconsistencies in the dataset inherited from the previous semester’s team.



Develop machine learning models with improved accuracy compared to the previous semester’s models.

Big Impact

By modeling community-level drivers of homelessness, this project enables:





Efficient resource allocation for assistance programs.



Identification of key socioeconomic factors influencing homelessness trends.



Timely policy interventions to reduce homelessness on a larger scale.



Repository Structure

This repository contains Python notebooks, datasets, and documentation for cleaning data and building predictive models. Below is an overview of the key files and their purposes.

Python Notebooks

Fix_Rent_+_Income.ipynb





Purpose: Processes American Community Survey (ACS) census tract data to correct errors in rent and income calculations.



Description:





Downloads ACS data (population [B01003_001E], rent [B25064_001E], income [B19013_001E]) directly from the U.S. Census Bureau.



Computes population-weighted averages for rent and income across CoCs using the formula: [ \text{Weighted Average} = \frac{\sum (\text{Value}_i \times \text{Population}_i)}{\sum \text{Population}_i} ]



Addresses the previous semester’s issue of summing values across census tracts, which led to inflated results (e.g., mean rent ~$186K, mean income ~$10.8M).



Output: Generates corrected_stuff.csv, a file containing accurate rent and income data for all CoCs.



Environment: Designed for Google Colab.

Regression_w_fixed_targets.ipynb





Purpose: Builds a linear regression model using the corrected dataset with normalized target variables and visualizes key insights.



Description:





Takes the final dataset with target variables normalized per 1,000 people using: [ \text{Normalized Target} = \left( \frac{\text{Raw Count}}{\text{Population}} \right) \times 1,000 ]



Creates a linear regression model to predict homelessness outcomes (e.g., overall homeless, sheltered homeless, unsheltered homeless, homeless individuals, homeless people in families).



Generates two visualizations:





Feature Correlation Plot: Shows correlations between input features (e.g., renter household rate, unemployment rate, weighted median rent) and homelessness outcomes. For example, renter household rate has the strongest correlation (~0.4).



Regression Coefficient Matrix: Displays standardized coefficients from five linear regression models (one per target variable), highlighting the direction and strength of each feature’s linear influence.



Environment: Designed for Google Colab.

Datasets

The project relies on ACS data from the U.S. Census Bureau for population, rent, and income calculations. Links to the datasets are provided below:





ACS Population Data: Total Population (B01003)



ACS Rent Data: Median Gross Rent (B25064)



ACS Income Data: Median Household Income (B19013)

Additional Data Notes





Point-in-Time (PIT) Data: Used for homelessness counts, merged with ACS data. Approximately 150 CoC-year pairs were lost during the merge due to mismatches in CoC boundaries (PIT data uses shifting boundaries, while ACS relies on fixed 2019/2022 census tract mappings).



Corrected Output: The corrected_stuff.csv file contains the population-weighted rent and income data, addressing discrepancies in the previous semester’s dataset.



Data Cleaning

The team addressed critical errors in the dataset:





Total Beds:





Issue: 42% missing data due to incorrect summation of Emergency Shelters, Transitional Housing, and Safe Havens.



Fix: Imputed zero for missing bed counts to ensure data integrity.



Rent and Income:





Issue: Inflated values from summing census tract data.



Fix: Computed population-weighted averages using ACS data.



Target Variables:





Issue: Inflated maximum values due to an erroneous “total homeless” row and incorrect normalization.



Fix: Removed the erroneous row and normalized targets per 1,000 people.



Model Development

Models Built





Linear Regression:





Simple and interpretable baseline model.



Performance improved slightly after normalizing target variables but remained limited due to its linear assumptions.



Neural Network:





Captures nonlinear interactions among features (e.g., rent, unemployment, temperature).



Fine-tuned with L2 regularization, dropout (20%), early stopping, and standardized features.



XGBoost:





(Details to be completed; likely chosen for handling nonlinear relationships).

Evaluation Metrics





Mean Absolute Error (MAE): Measures average prediction error magnitude, chosen over RMSE to avoid overweighting outliers.



R-squared (R²): Indicates how well the model explains variations in homelessness.



Exploratory Data Analysis





Correlation Analysis:





Strongest driver: Renter Household Rate (~0.4 correlation).



Other key factors: Cost Burdened Rate (~0.3), Unemployment Rate (~0.25), Weighted Median Rent (~0.2).



Homelessness Trends (2007–2023):





Total homelessness declined from ~800,000 (2007) to ~600,000 (2016), dipped to ~500,000 (2020), and spiked to >700,000 (2023).



Post-2020 surge driven by unsheltered homelessness.



Homeless People in Families:





Extreme socioeconomic conditions (e.g., high poverty, rent) correlate with higher homeless family counts.



Installation and Usage

Prerequisites





Python 3.8+



Google Colab (for running notebooks)



Required libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, tensorflow (for neural network)

Setup





Clone the repository:

git clone https://github.com/your-repo/community-homelessness-model.git



Install dependencies:

pip install -r requirements.txt



Open notebooks in Google Colab or a local Jupyter environment.

Running Notebooks





Fix_Rent_+_Income.ipynb:





Upload ACS data files or use provided links to download.



Run all cells to generate corrected_stuff.csv.



Regression_w_fixed_targets.ipynb:





Ensure corrected_stuff.csv and normalized target data are available.



Run all cells to train the linear regression model and generate visualizations.



Future Work





Resolve data loss from PIT-ACS merge by addressing CoC boundary mismatches.



Complete fine-tuning details for XGBoost and compare its performance.



Incorporate time-series models to capture temporal trends.



Validate models on held-out or future data.



Trace discrepancies in previous semester’s calculations using original data files.



Contributing

Contributions are welcome! Please submit issues or pull requests for bug fixes, feature additions, or documentation improvements. Ensure code follows PEP 8 guidelines and includes clear comments.

License

This project is licensed under the MIT License. See the LICENSE file for details.


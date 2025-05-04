The final data set for this team is CISS_final_df2 


Explanation for the following python files: 

Fix_Rent_+_Income.ipynb -> This google colab file processes ACS (American Community Survey) census tract data downloaded directly from the U.S. Census Bureau. It calculates the population-weighted average rent and income for all Continuums of Care (CoCs), allowing for more accurate comparisons and aggregations across geographic areas. The output of this correction was a file called "corrected_stuff.csv"


Regression_w_fixed_targets.ipynb -> This google colab file takes in the final data set with the fix targets (normalized to be per 1000 people) and created a linear regression model along with two graphs: one shows a feature correlation and the other shows a full regression coefficient matrix

Data Sets
ACS population data: https://data.census.gov/table?q=B01003:%20TOTAL%20POPULATION
ACS rent data: https://data.census.gov/table/ACSDT5YSPT2015.B25064
ACS income data: https://data.census.gov/table/ACSDT5Y2021.B19013?q=b19013&g=040XX00US50$0600000&codeset=p~true&t

The final data set for this team is CISS_final_df2 


Explanation for the following python files: 

Fix_Rent_+_Income.ipynb -> This google colab file processes ACS (American Community Survey) census tract data downloaded directly from the U.S. Census Bureau. It calculates the population-weighted average rent and income for all Continuums of Care (CoCs), allowing for more accurate comparisons and aggregations across geographic areas. The output of this correction was a file called "corrected_stuff.csv"


Regression_w_fixed_targets.ipynb -> This google colab file takes in the final data set with the fix targets (normalized to be per 1000 people) and created a linear regression model along with two graphs: one shows a feature correlation and the other shows a full regression coefficient matrix


import pandas as pd
import json

# Read the CSV file
df = pd.read_csv(r'C:\Users\ykks\Desktop\zuoye\spark\final_dataset.csv') 

# Group the data by CoC Name, Year, and Homelessness Type
grouped = df.groupby(['CoC Name', 'Year', 'Homelessness.Type'])['Count'].sum().unstack(level='Homelessness.Type').reset_index()

# Rename columns to match the expected format
grouped = grouped.rename(columns={
    'Overall.Homeless': 'Overall_Homeless',
    'Sheltered.Total.Homeless': 'Sheltered',
    'Unsheltered.Homeless': 'Unsheltered'
})

# Fill NaN values with 0
grouped = grouped.fillna(0)

# Convert data to the required format
data = grouped.to_dict('records')

# Create JavaScript code string
js_data = f"var data = {json.dumps(data)};"

# Read HTML template
with open('templates/index.html', 'r', encoding='utf-8') as file:
    html_template = file.read()

# Insert data into HTML template
html_with_data = html_template.replace('// INSERT_DATA_HERE', js_data)

# Write the result to a new HTML file
output_path = r'C:\Users\ykks\Desktop\zuoye\spark\Demo1\homeless_data_visualization.html'
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(html_with_data)

print(f"HTML file has been generated: {output_path}")

# Verify the data was inserted into the HTML
print("Data insertion verification:")
print("Data variable definition found:" if "var data = [" in html_with_data else "Data variable definition NOT found")
print("First data item found:" if str(data[0]) in html_with_data else "First data item NOT found")

# Print the first few items of the processed data
print("\nProcessed data sample:")
print(json.dumps(data[:5], indent=2))
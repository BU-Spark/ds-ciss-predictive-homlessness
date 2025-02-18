import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load dataset from CSV file"""
    df = pd.read_csv('/Users/kyle/Desktop/DS539/ds-ciss-predictive-homlessness-1/final_dataset.csv')
    print(f"Initial data shape: {df.shape}")
    return df

def clean_data(df):
    """Perform data cleaning operations"""
    # Handle missing values
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    # Fill or drop missing values based on columns
    df['CoC Category'] = df['CoC Category'].fillna('Unknown')
    df['Count Types'] = df['Count Types'].fillna('Not Specified')
    
    # Drop rows with missing critical numeric values
    df = df.dropna(subset=['Count'])
    
    # Convert count to integer
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce').astype('Int64')
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    return df

def perform_eda(df):
    """Perform exploratory data analysis"""
    # Basic statistics
    print("\nSummary Statistics:")
    print(df.describe())
    
    # Value counts for categorical columns
    print("\nCoC Categories Distribution:")
    print(df['CoC Category'].value_counts())
    
    # Time series analysis (if applicable)
    if 'Year' in df.columns:
        plt.figure(figsize=(12,6))
        sns.lineplot(x='Year', y='Count', data=df, estimator='sum')
        plt.title('Total Homeless Count Over Time')
        plt.show()
    
    # Distribution of counts
    plt.figure(figsize=(12,6))
    sns.histplot(df['Count'], bins=50, kde=True)
    plt.title('Distribution of Homeless Counts')
    plt.show()
    
    # Top 10 CoCs by total count
    top_cocs = df.groupby('CoC Name')['Count'].sum().nlargest(10)
    plt.figure(figsize=(12,6))
    top_cocs.plot(kind='barh')
    plt.title('Top 10 CoCs by Total Homeless Count')
    plt.xlabel('Total Count')
    plt.show()

if __name__ == "__main__":
    # Example usage
    df = load_data('final_dataset.csv')
    cleaned_df = clean_data(df)
    perform_eda(cleaned_df)
    cleaned_df.to_csv('cleaned_homelessness_data.csv', index=False) 
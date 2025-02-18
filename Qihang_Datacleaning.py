import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

matplotlib.use('TkAgg') 

def load_and_clean_data():
    """
    Load data from a CSV file, print basic info, remove duplicates,
    and fill missing values for both numeric and categorical columns.
    """
    # Load the dataset      
    df = pd.read_csv('/Users/kyle/Desktop/DS539/ds-ciss-predictive-homlessness-1/final_dataset.csv')
    print("Initial dataset shape:", df.shape)
    print(df.info())
    print(df.describe())
    
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    print("Shape after dropping duplicates:", df.shape)
    
    # Identify numeric and categorical columns
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    # Fill missing values for numeric columns with the median
    for col in num_cols:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
    
    # Fill missing values for categorical columns with the mode
    for col in cat_cols:
        mode_val = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
        df[col].fillna(mode_val, inplace=True)
    
    print("Missing values after cleaning:")
    print(df.isnull().sum())
    
    return df

def basic_eda_plots(df):
    """
    Generate basic exploratory data analysis (EDA) plots:
    - Histograms and KDE plots for numeric variables.
    - Boxplots for numeric variables.
    - Countplots for categorical variables.
    - Pairplot for numeric variables.
    - Correlation heatmap for all numeric variables.
    """
    sns.set(style="whitegrid")
    
    # Identify numeric and categorical columns
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    # Plot histogram with KDE for each numeric column
    for col in num_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], kde=True, color='blue', edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()
    
    # Plot boxplot for each numeric column
    for col in num_cols:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[col], color='lightgreen')
        plt.title(f'Boxplot of {col}')
        plt.xlabel(col)
        plt.show()
    
    # Plot countplot for each categorical column
    for col in cat_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=col, data=df, palette='pastel')
        plt.title(f'Countplot of {col}')
        plt.xlabel('Count')
        plt.ylabel(col)
        plt.show()
    
    # Plot pairplot for numeric columns (if there are at least 2)
    if len(num_cols) >= 2:
        sns.pairplot(df[num_cols], diag_kind="kde")
        plt.suptitle('Pairplot of Numeric Variables', y=1.02)
        plt.show()
    
    # Plot correlation heatmap for all numeric columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap of All Numeric Variables')
    plt.show()

def top15_correlation_heatmap(df):
    """
    Identify the top 15 variables based on the sum of absolute correlations
    with other variables (ignoring self-correlation) and plot their correlation heatmap.
    """
    # Select numeric columns
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    corr_matrix = df[num_cols].corr()
    
    # Set the diagonal to zero to ignore self-correlation in scoring
    corr_matrix_no_diag = corr_matrix.copy()
    np.fill_diagonal(corr_matrix_no_diag.values, 0)
    
    # Calculate a score for each variable (sum of absolute correlations with other variables)
    corr_scores = corr_matrix_no_diag.abs().sum().sort_values(ascending=False)
    top15_vars = corr_scores.head(15).index.tolist()
    
    print("Top 15 variables with the highest overall correlation:")
    print(top15_vars)
    
    # Plot heatmap for the top 15 variables
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[top15_vars].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Heatmap of Top 15 Variables")
    plt.show()

def perform_eda(df):
    """Enhanced EDA with comprehensive visualizations"""
    plt.figure(figsize=(10, 6))
    
    # 1. Time Series Analysis (if Year column exists)
    if 'Year' in df.columns:
        # Monthly/Yearly trends with error bands
        plt.figure(figsize=(14, 7))
        sns.lineplot(x='Year', y='Count', data=df, 
                    estimator='median', errorbar=('ci', 95),
                    color='darkred', linewidth=2.5)
        plt.title('Yearly Homeless Count Trends with 95% CI')
        plt.ylabel('Median Count')
        plt.show()
        
        # Seasonal decomposition
        from statsmodels.tsa.seasonal import seasonal_decompose
        ts_data = df.groupby('Year')['Count'].median()
        decomposition = seasonal_decompose(ts_data, period=1)
        decomposition.plot()
        plt.suptitle('Time Series Decomposition')
        plt.tight_layout()
        plt.show()

    # 2. Categorical-Numeric Relationships
    if 'CoC Category' in df.columns:
        # Boxplot by category
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='Count', y='CoC Category', data=df,
                   palette='viridis', showfliers=False)
        plt.title('Count Distribution by CoC Category')
        plt.show()
        
        # Violin plot with swarm overlay
        plt.figure(figsize=(12, 6))
        sns.violinplot(x='CoC Category', y='Count', data=df,
                      inner=None, palette='coolwarm')
        sns.swarmplot(x='CoC Category', y='Count', data=df,
                     color='black', alpha=0.5, size=2)
        plt.xticks(rotation=45)
        plt.title('Category Distribution with Data Points')
        plt.show()

    # 3. Advanced Correlation Analysis
    numeric_cols = df.select_dtypes(include=np.number).columns
    if len(numeric_cols) > 1:
        # Scatter matrix with regression lines
        sns.pairplot(df[numeric_cols], kind='reg', 
                    plot_kws={'line_kws':{'color':'red'}, 
                             'scatter_kws': {'alpha': 0.3}})
        plt.suptitle('Scatter Matrix with Regression Lines', y=1.02)
        plt.show()
        
        # Cluster heatmap
        corr = df[numeric_cols].corr()
        sns.clustermap(corr, cmap='coolwarm', annot=True, 
                      figsize=(12, 10), standard_scale=1)
        plt.title('Clustered Correlation Heatmap')
        plt.show()

    # 4. Advanced Categorical Analysis
    if 'Count Types' in df.columns:
        # Stacked percentage bar plot
        pd.crosstab(df['CoC Category'], df['Count Types'], 
                   normalize='index').plot.barh(
                       stacked=True, figsize=(12, 8))
        plt.title('Category Composition by Count Type')
        plt.xlabel('Percentage')
        plt.ylabel('CoC Category')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()

    # 5. Interactive Visualizations (if needed)
    # Uncomment to use Plotly interactive plots
    # import plotly.express as px
    # fig = px.scatter(df, x='Year', y='Count', color='CoC Category',
    #                 size='Count', hover_data=['Count Types'])
    # fig.show()

def main():
    # Replace 'data.csv' with the path to your dataset if needed
    df = load_and_clean_data()
    
    # Generate basic EDA plots
    basic_eda_plots(df)
    
    # Generate and display the correlation heatmap for the top 15 variables
    top15_correlation_heatmap(df)

    # Perform enhanced EDA
    perform_eda(df)

if __name__ == "__main__":
    main()

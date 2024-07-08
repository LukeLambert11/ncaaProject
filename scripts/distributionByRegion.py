import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def graph(df: pd.DataFrame, year: int) -> None:
    
    filtered_df = df.copy()
    # Drop rows with missing values in the relevant columns
    filtered_df.dropna(subset=['ncaaPlace', 'regionPlace'], inplace=True)

    # Ensure 'ncaaPlace' is numeric
    filtered_df = filtered_df[filtered_df['ncaaPlace'] != 'DNF']
    filtered_df['ncaaPlace'] = pd.to_numeric(filtered_df['ncaaPlace'])

    # Plotting
    plt.figure(figsize=(12, 8))

    # Box plot for ncaaPlace per region
    sns.boxplot(x='region', y='ncaaPlace', data=filtered_df)
    plt.title(f'{year} NCAA Place Distribution by Region')
    plt.xlabel('Region')
    plt.ylabel('NCAA Place')

    plt.tight_layout()
    plt.show()
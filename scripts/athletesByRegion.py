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

    # Calculate the number of athletes for each region
    region_counts = filtered_df['region'].value_counts().reset_index()
    region_counts.columns = ['region', 'num_athletes']

    # Plotting
    plt.figure(figsize=(12, 8))

    # Bar plot for the number of athletes per region
    barplot = sns.barplot(x='region', y='num_athletes', data=region_counts)
    plt.title(f'Number of Athletes by Region {year}')
    plt.xlabel('Region')
    plt.ylabel('Number of Athletes')

    # Add values on top of each bar
    for index, row in region_counts.iterrows():
        barplot.text(row.name, row.num_athletes, round(row.num_athletes, 2), color='black', ha="center")


    plt.tight_layout()
    plt.show()
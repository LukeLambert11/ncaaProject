import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def graph(df: pd.DataFrame, year: int) -> None:

    # Assuming df is your dataframe
    filtered_df = df.copy()
    # Drop rows with missing values in the relevant columns
    filtered_df.dropna(subset=['ncaaPlace', 'ncaaPriorPlace'], inplace=True)

    # Ensure 'ncaaPlace' and 'ncaaPriorPlace' are numeric
    filtered_df = filtered_df[filtered_df['ncaaPlace'] != 'DNF']
    filtered_df = filtered_df[filtered_df['ncaaPriorPlace'] != 'DNF']
    filtered_df['ncaaPlace'] = pd.to_numeric(filtered_df['ncaaPlace'])
    filtered_df['ncaaPriorPlace'] = pd.to_numeric(filtered_df['ncaaPriorPlace'])

    # Calculate the change in placement
    filtered_df['change_in_place'] = filtered_df['ncaaPriorPlace'] - filtered_df['ncaaPlace']

    # Determine the top half and back half placements
    mid_point = df['ncaaPlace'].max() / 2
    print(mid_point)
    top_half_df = filtered_df[filtered_df['ncaaPlace'] <= mid_point]
    back_half_df = filtered_df[filtered_df['ncaaPlace'] > mid_point]

    # Calculate the mean and median change in placement for all athletes, top half athletes, and back half athletes
    average_change_all = filtered_df['change_in_place'].mean()
    median_change_all = filtered_df['change_in_place'].median()

    average_change_top_half = top_half_df['change_in_place'].mean()
    median_change_top_half = top_half_df['change_in_place'].median()

    average_change_back_half = back_half_df['change_in_place'].mean()
    median_change_back_half = back_half_df['change_in_place'].median()

    # Create a dataframe for plotting
    average_changes = pd.DataFrame({
        'Category': ['All Athletes', 'All Athletes', 'Top Half Athletes', 'Top Half Athletes', 'Back Half Athletes', 'Back Half Athletes'],
        'Metric': ['Mean', 'Median', 'Mean', 'Median', 'Mean', 'Median'],
        'Change in Placement': [
            average_change_all, median_change_all,
            average_change_top_half, median_change_top_half,
            average_change_back_half, median_change_back_half
        ]
    })

    # Plotting
    plt.figure(figsize=(14, 8))

    # Bar plot for the average and median change in placement
    barplot = sns.barplot(x='Category', y='Change in Placement', hue='Metric', data=average_changes)
    plt.title(f'Mean and Median Change in Placement from {year} NCAA Prior Place ({year-1})')
    plt.xlabel('Placement Group')
    plt.ylabel('Change in Placement')

    # Add values on top of each bar
    for bar in barplot.patches:
        height = bar.get_height()
        if height != 0:
            barplot.annotate(format(height, '.2f'),
                            (bar.get_x() + bar.get_width() / 2, height),
                            ha = 'center', va = 'center',
                            size=10, xytext = (0, 8),
                            textcoords = 'offset points')

    plt.tight_layout()
    plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

def graph(df: pd.DataFrame, year: int) -> None:

    filtered_df = df.copy()
    filtered_df.dropna(subset=['ncaaPlace', 'ncaaPriorPlace'], inplace=True)
    filtered_df = filtered_df[filtered_df['ncaaPlace'] != 'DNF']

    filtered_df = filtered_df.sort_values(by='ncaaPlace')
    num_points = len(filtered_df)


    plt.figure(figsize=(10, 6))
    plt.scatter(filtered_df['ncaaPlace'], filtered_df['ncaaPriorPlace'], color='blue', label=f'Data Points (n={num_points})')

    plt.xlabel(f'NCAA Place ({year})')
    plt.ylabel(f'Ncaa Prior Place ({year-1})')
    plt.title(f'Comparison of NCAA Place and Ncaa Prior Place ({year})')
    plt.title('Comparison of NCAA Place and Ncaa Prior Place')
    plt.grid(True)

    # Linear regression
    linear_coeffs = np.polyfit(filtered_df['ncaaPlace'], filtered_df['ncaaPriorPlace'], 1)
    linear_regression_line = np.polyval(linear_coeffs, filtered_df['ncaaPlace'])
    plt.plot(filtered_df['ncaaPlace'], linear_regression_line, color='red', linestyle='--', label=f'Linear Regression (R²={r2_score(filtered_df["ncaaPriorPlace"], linear_regression_line):.4f})')

    # Quadratic regression
    quadratic_coeffs = np.polyfit(filtered_df['ncaaPlace'], filtered_df['ncaaPriorPlace'], 2)
    quadratic_regression_line = np.polyval(quadratic_coeffs, filtered_df['ncaaPlace'])
    plt.plot(filtered_df['ncaaPlace'], quadratic_regression_line, color='green', linestyle='--', label=f'Quadratic Regression (R²={r2_score(filtered_df["ncaaPriorPlace"], quadratic_regression_line):.4f})')

    # Calculate R-squared for linear regression
    linear_r2 = r2_score(filtered_df['ncaaPriorPlace'], linear_regression_line)

    # Calculate R-squared for quadratic regression
    quadratic_r2 = r2_score(filtered_df['ncaaPriorPlace'], quadratic_regression_line)

    # Print R² values
    print(f"Linear Regression R-squared: {linear_r2:.4f}")
    print(f"Quadratic Regression R-squared: {quadratic_r2:.4f}")


    plt.legend()
    plt.show()
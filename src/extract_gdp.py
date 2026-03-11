# import numpy as np
# import pandas as pd

# # URL of the archived Wikipedia page
# URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# # Extract tables from webpage
# tables = pd.read_html(URL)

# # Select the required table
# df = tables[3]

# # Replace column headers with column numbers
# df.columns = range(df.shape[1])

# # Keep only Country and IMF GDP column
# df = df[[0, 2]]

# # Keep only top 10 economies
# df = df.iloc[1:11, :]

# # Rename columns
# df.columns = ["Country", "GDP (Million USD)"]

# # Convert GDP to integer
# df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(int)

# # Convert Million → Billion
# df["GDP (Million USD)"] = df["GDP (Million USD)"] / 1000

# # Round values
# df["GDP (Million USD)"] = np.round(df["GDP (Million USD)"], 2)

# # Rename column
# df.rename(columns={"GDP (Million USD)": "GDP (Billion USD)"}, inplace=True)

# # Save CSV
# df.to_csv("Largest_economies.csv", index=False)
# df = df.sort_values(by="GDP (Billion USD)", ascending=False)
# print("CSV file successfully created!")
# print(df)


import numpy as np
import pandas as pd

URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"


def extract_data(url):
    tables = pd.read_html(url)
    df = tables[3]
    return df


def transform_data(df):

    df.columns = range(df.shape[1])
    df = df[[0, 2]]
    df = df.iloc[1:11, :]

    df.columns = ["Country", "GDP (Million USD)"]

    df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(int)

    df["GDP (Million USD)"] = df["GDP (Million USD)"] / 1000
    df["GDP (Million USD)"] = np.round(df["GDP (Million USD)"], 2)

    df.rename(columns={"GDP (Million USD)": "GDP (Billion USD)"}, inplace=True)

    return df


def load_data(df):
    df.to_csv("Largest_economies.csv", index=False)


def main():

    df = extract_data(URL)

    df = transform_data(df)

    load_data(df)

    print("CSV file successfully created")
    print(df)


if __name__ == "__main__":
    main()
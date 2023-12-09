import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Pivot the DataFrame to create the matrix
    matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    # Set diagonal values to 0
    for i in range(len(matrix)):
        matrix.iloc[i, i] = 0
    
    return matrix


def get_type_count(df) -> dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame): Input DataFrame containing the 'car' column.

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Add a new categorical column 'car_type' based on 'car' values
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=['low', 'medium', 'high'])
    
    # Calculate the count of occurrences for each car_type category
    type_count = df['car_type'].value_counts().to_dict()
    
    # Sort the dictionary alphabetically based on keys
    sorted_type_count = {k: type_count[k] for k in sorted(type_count)}
    
    return sorted_type_count

# Assuming 'dataset-1.csv' is in the same directory as your Python script
# Load the CSV file into a DataFrame
df = pd.read_csv('dataset-1.csv')

# Use the function to get the count of car_type occurrences
result = get_type_count(df)
print(result)



def get_bus_indexes(df) -> list:
    """
    Identifies indices where the 'bus' values are greater than twice the mean value of the 'bus' column.

    Args:
        df (pandas.DataFrame): Input DataFrame containing the 'bus' column.

    Returns:
        list: A list of indices (sorted in ascending order) where 'bus' values are greater than twice the mean.
    """
    # Calculate the mean of the 'bus' column
    mean_bus = df['bus'].mean()
    
    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    
    # Sort the indices in ascending order
    bus_indexes.sort()
    
    return bus_indexes



def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()

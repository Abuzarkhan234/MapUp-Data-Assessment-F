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



def filter_routes(df) -> list:
    """
    Filters routes based on the average of 'truck' column values and returns a sorted list of routes.

    Args:
        df (pandas.DataFrame): Input DataFrame containing the 'route' and 'truck' columns.

    Returns:
        list: A sorted list of values in the 'route' column for which the average of 'truck' column values is greater than 7.
    """
    # Calculate the average of 'truck' column values for each route
    route_avg_truck = df.groupby('route')['truck'].mean()
    
    # Filter routes where the average of 'truck' column values is greater than 7
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    
    # Sort the list of routes
    filtered_routes.sort()
    
    return filtered_routes


def multiply_matrix(matrix_df) -> pd.DataFrame:
    """
    Modifies values in the input DataFrame based on specified conditions and returns the modified DataFrame.

    Args:
        matrix_df (pandas.DataFrame): Input DataFrame generated from Question 1.

    Returns:
        pandas.DataFrame: Modified DataFrame with values adjusted according to specified conditions.
    """
    # Apply value modifications based on conditions
    modified_df = matrix_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    
    # Round values to 1 decimal place
    modified_df = modified_df.round(1)
    
    return modified_df

def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
     # Convert 'timestamp' column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Extract day and time components
    df['day'] = df['timestamp'].dt.day_name()
    df['time'] = df['timestamp'].dt.time

    # Group by 'id' and 'id_2', check if the timestamps cover a full 24-hour period and span all 7 days
    completeness_check = df.groupby(['id', 'id_2']).apply(lambda x: (set(x['day']) == set(calendar.day_name)) and (x['time'].min() <= pd.Timestamp('23:59:59').time()) and (x['time'].max() >= pd.Timestamp('00:00:00').time()))

    return completeness_check

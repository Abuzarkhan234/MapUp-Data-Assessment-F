import pandas as pd



df = pd.read_csv('dataset-3.csv')

def calculate_distance_matrix(df) -> pd.DataFrame:
    """
    Generates a DataFrame representing distances between IDs.

    Args:
        df (pandas.DataFrame): Input DataFrame with columns 'id_start', 'id_end', and 'distance'.

    Returns:
        pandas.DataFrame: DataFrame representing cumulative distances between IDs.
    """
    # Create an empty DataFrame to store distances
    unique_ids = sorted(set(df['id_start']).union(set(df['id_end'])))
    distance_matrix = pd.DataFrame(0, index=unique_ids, columns=unique_ids)

    # Loop through the dataset to calculate distances
    for _, row in df.iterrows():
        start = row['id_start']
        end = row['id_end']
        distance = row['distance']

        # Update distances in both directions
        distance_matrix.at[start, end] = distance
        distance_matrix.at[end, start] = distance

    # Calculate cumulative distances
    for i in unique_ids:
        for j in unique_ids:
            for k in unique_ids:
                if distance_matrix.at[i, j] > 0 and distance_matrix.at[j, k] > 0:
                    if distance_matrix.at[i, k] == 0 or distance_matrix.at[i, k] > distance_matrix.at[i, j] + distance_matrix.at[j, k]:
                        distance_matrix.at[i, k] = distance_matrix.at[i, j] + distance_matrix.at[j, k]

    return distance_matrix
result = calculate_distance_matrix(df)

# Display the resulting distance matrix
print(result)



def unroll_distance_matrix(distance_matrix) -> pd.DataFrame:
    """
    Unrolls the distance matrix DataFrame into id_start, id_end, and distance columns.

    Args:
        distance_matrix (pandas.DataFrame): DataFrame representing cumulative distances between IDs.

    Returns:
        pandas.DataFrame: DataFrame containing id_start, id_end, and distance columns.
    """
    unrolled_distances = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            # Exclude identical id_start and id_end pairs
            if id_start != id_end:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_distances.append([id_start, id_end, distance])

    unrolled_df = pd.DataFrame(unrolled_distances, columns=['id_start', 'id_end', 'distance'])
    return unrolled_df



def find_ids_within_ten_percentage_threshold(df, reference_value):
    """
    Calculates the average distance for a reference value and returns a sorted list
    of values from the id_start column within 10% of the reference value's average.

    Args:
    df (pandas.DataFrame): DataFrame with columns 'id_start', 'id_end', and 'distance'.
    reference_value (int): The reference value from the id_start column.

    Returns:
    list: Sorted list of values from id_start column within the 10% threshold.
    """
    # Calculate the average distance for the reference value
    avg_distance = df[df['id_start'] == reference_value]['distance'].mean()

    # Calculate the threshold range
    threshold = avg_distance * 0.1

    # Find values within the threshold range
    within_threshold = df[(df['distance'] >= (avg_distance - threshold)) & (df['distance'] <= (avg_distance + threshold))]['id_start'].unique()

    return sorted(within_threshold)




def calculate_toll_rate(df):
    """
    Calculates toll rates based on vehicle types and adds corresponding columns
    to the input DataFrame with rate coefficients.

    Args:
    df (pandas.DataFrame): DataFrame with columns 'id_start', 'id_end', and 'distance'.

    Returns:
    pandas.DataFrame: DataFrame with added columns for toll rates for each vehicle type.
    """
    # Calculate toll rates based on vehicle types
    df['moto'] = df['distance'] * 0.8
    df['car'] = df['distance'] * 1.2
    df['rv'] = df['distance'] * 1.5
    df['bus'] = df['distance'] * 2.2
    df['truck'] = df['distance'] * 3.6

    return df




from datetime import time

# Define the calculate_distance_matrix function
# Define the unroll_distance_matrix function
# Define the find_ids_within_ten_percentage_threshold function
# Define the calculate_toll_rate function

def calculate_time_based_toll_rates(df):
    """
    Calculates toll rates for different time intervals within a day and adds
    the appropriate columns to the input DataFrame.

    Args:
    df (pandas.DataFrame): DataFrame with columns 'id_start', 'id_end', and 'distance'.

    Returns:
    pandas.DataFrame: DataFrame with added columns for time-based toll rates.
    """
    # Define time ranges
    weekdays_discounts = {
        time(0, 0, 0): 0.8,
        time(10, 0, 0): 1.2,
        time(18, 0, 0): 0.8,
        time(23, 59, 59): 0.8
    }

    weekends_discount = 0.7

    # Add columns for time-based toll rates
    df['start_day'] = 'Monday'  # Set as an example; change as needed
    df['end_day'] = 'Sunday'    # Set as an example; change as needed
    df['start_time'] = time(8, 0, 0)  # Set as an example; change as needed
    df['end_time'] = time(20, 0, 0)   # Set as an example; change as needed

    # Calculate toll rates based on time intervals
    for index, row in df.iterrows():
        start_time = row['start_time']
        end_time = row['end_time']
        start_day = row['start_day']
        end_day = row['end_day']
        vehicle_types = ['moto', 'car', 'rv', 'bus', 'truck']

        # Check if it's a weekday or weekend
        if start_day in weekdays_discounts and end_day in weekdays_discounts:
            for vehicle_type in vehicle_types:
                # Apply discount based on time range
                discount_factor = 0
                for time_range, discount in weekdays_discounts.items():
                    if start_time >= time_range and end_time <= time_range:
                        discount_factor = discount

                # Apply discount to toll rates
                df.at[index, vehicle_type] *= discount_factor
        else:
            # Apply constant weekend discount for all times
            for vehicle_type in vehicle_types:
                df.at[index, vehicle_type] *= weekends_discount

    return df

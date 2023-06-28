import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': r'\\bsh.corp.bshg.com\fredirect\SK\KOS\Pelletier\Documents\Python\udacity\chicago.csv',
              'new york city': r'\\bsh.corp.bshg.com\fredirect\SK\KOS\Pelletier\Documents\Python\udacity\new_york_city.csv',
              'washington': r'\\bsh.corp.bshg.com\fredirect\SK\KOS\Pelletier\Documents\Python\udacity\washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june','all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']

def display_dictionary_keys(dictionary):
    keys = dictionary.keys()
    for key in keys:
        print(key)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('The data for the cities below are available.Press Q to quit.')
        display_dictionary_keys(CITY_DATA)

        city = input("Enter a city name: ").lower()
        if city in CITY_DATA:
            print("City found:", city)
            break
        elif city == 'q':
            return
        else:
            print("City not found. Please try again.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter a month (January to June) or all. Press Q to quit.: ").lower()
        if month in MONTH_DATA:
            print("Valid month:", month)
            break
        elif city == 'q':
            return
        else:
            print("Invalid month. Please try again.")



    # get user input for day of week (all, monday, tuesday, ... sunday)


    while True:
        day = input("Enter a day of the week (Monday to Sunday) or all: ").lower()
        if day in DAY_DATA :
            print("Valid day:", day)

            break
        else:
            print("Invalid day. Please try again.")

    print('-'*40)
    return city, month, day


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

def load_data(city, month, day):
    # Load the city data into a DataFrame

    filename = CITY_DATA.get(city.lower())
    df = pd.read_csv(filename)

    # Convert the "Start Time" column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if applicable
    if month.lower() != 'all':
        # Extract the month from the "Start Time" column
        df['Month'] = df['Start Time'].dt.month

        # Filter the DataFrame by the specified month

        month_index = MONTH_DATA.index(month.lower()) + 1
        df = df[df['Month'] == month_index]

    # Filter by day if applicable
    if day.lower() != 'all':
        # Extract the day of the week from the "Start Time" column
        df['Day of Week'] = df['Start Time'].dt.dayofweek

        # Map the day of the week to the corresponding name
        day_index = DAY_DATA.index(day.lower())
        df = df[df['Day of Week'] == day_index]

    print(df.shape)

 
    return df

def display_data(df):
    start_loc = 0
    while True:
        display = input("Do you want to see 5 rows of data? Enter 'yes' or 'no': ")
        if display.lower() == 'yes':
            print(df.iloc[start_loc : start_loc+5])
            start_loc += 5
        elif display.lower() == 'no':
            break
        else:
            print("Invalid input. Please try again.")
            
def time_stats(df):
    print('timestat')
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
  # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour from the 'Start Time' column
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour

    # Display the most common month
    common_month = df['Month'].mode()[0]
    print('Most Common Month:', common_month)

    # Display the most common day of the week
    common_day_of_week = df['Day of Week'].mode()[0]
    print('Most Common Day of Week:', common_day_of_week)

    # Display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # Display the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # Display the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)

    # Display the most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most Frequent Trip (Start Station -> End Station):', common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

  # Display the total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display the mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

# Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of User Types:')
    print(user_type_counts)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)
    else:
        print('\nGender information not available.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarliest Birth Year:', earliest_birth_year)
        print('Most Recent Birth Year:', most_recent_birth_year)
        print('Most Common Birth Year:', most_common_birth_year)
    else:
        print('\nBirth year information not available.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

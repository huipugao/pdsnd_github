import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'febuary', 'march', 'april', 'may', 'june']
DAY_DATA = ['all','monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). While loop is used to handle invalid inputs
    print('Welcome to this program')
    city=input("Please select your city(Chicago, New York City, Washington): ").lower()
    while city not in CITY_DATA.keys():
        city=input("Sorry we are not able to get the city data. Please input Chicago, New York City, or Washington: ").lower()

    # get user input for month (all, january, february, ... , june) While loop is used to handle invalid inputs
    print('What is the month you are intested in? You can select all, january, february, ... , june')
    month=input("Please input the month to filter data:").lower()
    while month not in MONTH_DATA:
        month=input("Sorry we are not able to get the month data. Please input all, january, february, ... , or june: ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('What is the day you are intested in? You can select all, monday, tuesday, ... sunday')
    day=input("Please input the day to filter data:").lower()
    while day not in DAY_DATA:
        day=input("Sorry we are not able to get the day data. Please input all, monday, tuesday, ..., or sunday: ").lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month of travel is {}'.format(MONTH_DATA[popular_month]))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is {}'.format(popular_day))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is{}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is{}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    station_combination = (" From " + df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('The most popular trip is{}'.format(station_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in hours
    total_travel_time = df['Trip Duration'].sum()/3600
    print(f"The total trip duration is {total_travel_time} hours.")

    #  display mean travel time in minutes
    mean_travel_time = df['Trip Duration'].mean()/60
    print("The average travel time is {mean_travel_time} minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types are:\n{}\n'.format(user_types))
    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('The counts of user gender is:\n{}\n'.format(gender))
    # Display earliest, most recent, and most common year of birth
        earliest_birth_year=df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print(' The earliest year of birth is {}\n The most recent of birth is {}\n The most common year of birht is {}'.format(earliest_birth_year, most_recent_birth_year, most_common_birth_year))
    except:
          print('the birth data is not avaialbe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def view_data(df):
    """ Display 5 rows of data for the selected city if requested """
    row_index = 0
    answer_data = input('Do you want to view raw data? Please input yes or no \n').lower()
    while answer_data not in ['yes','no']:
        print('We are not able to recognize the input, please select yes or no')
        answer_data=input().lower()
    while True:
        if answer_data == 'no':
            return
        if answer_data == 'yes':
            print(df[row_index: row_index+5])
            row_index+=5
            answer_data = input('Would you like to view more data? pleaer input yes or no \n').lower()
            while answer_data not in ['yes','no']:
                print('We are not able to recognize the input, please select yes or no')
                answer_data=input().lower()
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

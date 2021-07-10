# Done by ZayedAlharthi for Programming for Data Science with Python Nanodegree at Udacity
# https://github.com/ZayedAlharthi/pdsnd_github
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city should we investigate? (chicago, new york city, or washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Please enter a valid city name')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month should we filter by? (all, january, february, ... , june): ').lower()
        if month in months:
            break
        else:
            print('Please enter a valid month name or all for all months')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day should we filter by? (all, monday, tuesday, ... sunday): ').lower()
        if day in days:
            break
        else:
            print('Please enter a valid day name or all for all days')

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df[df['month'] == months.index(month)]
    if day != 'all':
        df = df[df['day_of_week'] == days.index(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts()
    print("The most common month is: {} with a count of {}".format(months[common_month.index[0]].title(),common_month.values[0]))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts()
    print("The most common day is: {} with a count of {}".format(days[common_day.index[0]].title(), common_day.values[0]))

    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts()
    print("The most common hour is: {} with a count of {}".format(common_hour.index[0], common_hour.values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts()
    print('The most common Start Station is: {} with a count of {}'.format(common_start_station.index[0],common_start_station.values[0]))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts()
    print('The most common End Station is: {} with a count of {}'.format(common_end_station.index[0],common_end_station.values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most common combination of start station and end station is: Start Station: {}, End Station: {}'.format(common_start_end_station[0],common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: {} seconds'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    for Utype, count in enumerate(user_types):
        print('User Type: {} has a count of: {} users'.format(user_types.index[Utype], count))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        for gender, count in enumerate(genders):
            print('Gender: {} has a count of {}'.format(genders.index[gender], count))
    else:
        print("No gender data to show")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        common_yob = df['Birth Year'].value_counts().index[0]
        earliest_yob = df['Birth Year'].min()
        recent_yob = df['Birth Year'].max()
        print('The earliest year of birth is: {}\nMost recent year of birth is: {}\nMost common year of birth is: {}'.format(earliest_yob,recent_yob,common_yob))
    else:
        print("No birth year data to show")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    view_raw_data = input('Would you like to view the first 5 raw data? Enter yes or no.\n ')
    if view_raw_data.lower() != 'no':
        index = 0
        while True:
            print(df.iloc[index:index + 5])
            view_more_raw_data = input('Would you like to view the next 5 raw data? Enter yes or no. \n ')
            if view_more_raw_data != 'no':
                index +=5
            else:
                return
    else:
        return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

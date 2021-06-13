import time
import pandas as pd
import numpy as np
import json


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Lets explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input("Please submit your input selection from Chicago, New York City or Washington? \n> ").lower()
       if city in CITIES:
           break

    # TO DO: get user input for month (all, january, february, ... , june)
    #Get user input for their choice of month of the year
    month = get_user_input("Please type a month of your choice from january to june for analysis"\
                    "or type in \'all\' to apply no month filter. \n(e.g. all, january, february, march, april, may, june) \n> ", MONTHS)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Get the input from the user for their choice of the day of week
    day = get_user_input("Please type one of the week day for analysis or type in \'all\' to apply no day filter. \n(e.g. all, sunday, monday, tuesday, wednesday, thursday, friday, saturday) \n> ", DAYS)

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        #Using title() to convert the first character in each word to Uppercase and keeping the remaining characters to Lowercase in the string and returning a new string
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()
    
    # TO DO: display the most common month
    #DISPLAYING THE MOST COMMON MONTH
    #Using df. idxmax() to find the index of the max value of a Pandas DataFrame column
    most_common_month = df['month'].value_counts().idxmax()
    print("\nMost common month:", most_common_month)

    # TO DO: display the most common day of week
    #DISPLAYING THE MOST COMMON DAY OF THE WEEK
    #Using df. idxmax() to find the index of the max value of a Pandas DataFrame column
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("\nMost common day of the week :",most_common_day_of_week)

    # TO DO: display the most common start hour
    #DISPLAYING THE MOST COMMON START HOUR
    #Using df. idxmax() to find the index of the max value of a Pandas DataFrame column
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("\nMost common start hour :",round(most_common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #DISPLAYING MOST COMMONLY USED START STATION
    #Using df. idxmax() to find the index of the max value of a Pandas DataFrame column
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most used start: ", most_common_used_start_station)
    

    # TO DO: display most commonly used end station
    #DISPLAYING MOST COMMONLY USED END STATION
    #Using df. idxmax() to find the index of the max value of a Pandas DataFrame column
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("Most used end: ", most_common_used_end_station)
    
    
    # TO DO: display most frequent combination of start station and end station trip
    #DISPLAYING MOST FREQUENT COMBINATION OF START STATION AND END STATION
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("\nMost frequent combination of start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))
    
    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*40)


#Function for trip duration related statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Uses sum method to calculate the total trip duration
    total_duration = df['Trip Duration'].sum()
    #Finds out the duration in minutes and seconds format
    minute, second = divmod(total_duration, 60)
    #Finds out the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    #Calculating the average trip duration using mean method
    average_duration = round(df['Trip Duration'].mean())
    #Finds the average duration in minutes and seconds format
    mins, sec = divmod(average_duration, 60)
    #This filter prints the time in hours, mins, sec format if the mins exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:\n", user_counts)
    
    # TO DO: Display counts of gender
    if "Gender" in df:
        print("\nCounts concerning client`s gender")
        print("\nFemale population: ", df.query("Gender == 'Female'").Gender.count())
        print("\nMale population: ", df.query("Gender == 'Male'").Gender.count())

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("\nEarliest year of birth: ", int(df["Birth Year"].min()))
        print("\nMost recent year of birth: ", int(df["Birth Year"].max()))
        print("\nMost common year of birth: ", int(df["Birth Year"].value_counts().idxmax()))


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*40)
    
def get_user_input(message, user_input_options):
    """
    An utility function to obtain user specific input value
    Args:
        (str) message - an information message for a particular request
    Returns:
        (str) user_data - requested data from user
    """

    while True:
        user_data = input(message).lower()
        if user_data in user_input_options:
            break
        if user_data == 'all':
            break
    
    return user_data

def display_raw_data(df):
    """Displays raw bikeshare data."""
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 10):
        
        a = input("\nWould you like to examine the particular user trip data?However, it will all be displayed as Unnamed as there is no name given in the csv, Type \'yes\' or \'no\'\n")
        if a.lower() != 'yes':
            break
        
        # retrieve and convert data to json format
        # split each json row data 
        row_values = df.iloc[i: i + 10].to_json(orient='records', lines=True).split('\n')
        for row in row_values:
            # pretty print each user data
            parsed_row_values = json.loads(row)
            json_row_data = json.dumps(parsed_row_values, indent=2)
            print(json_row_data)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':  
           break

if __name__ == "__main__":
	main()

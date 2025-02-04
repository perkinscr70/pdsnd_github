import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
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
        cities = ['chicago','new york city','washington']
        city = input("\nPlease select a city for which you would like to see the statistics from one of the following: Chicago, New York City or Washington: ").strip().lower()

        if city in cities:
            break
        else: print("\nPlease try again, you may have misspelled or picked a city not in the list.")
                  

    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['all','january','february','march','april','may','june']
        month = input("\n Please select a month from one of the following: January, February, March, April, May or June: ").strip().lower()
        
        if month in months:
            break
        else: print("\n Please try again, you may have misspelled or picked a month that we do not have data for.")
   
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = input("\n Please select a day of the week you would like to see the statistics for: ").strip().lower()

        if day in days:
            break
        else: print("\n Please try again, you may have misspelled.")

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
    # Load City data into DataFrame
    df = pd.read_csv(CITY_DATA[city])
    
    #print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month from the Start Time column to create month column
    df['month'] = df['Start Time'].dt.month
    
    #Extract Day from Start Time column to create Day column
    df['day'] = df['Start Time'].dt.day_name()
   
    #Extract Hour from Start Time column to create Hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of months list to get the corresponding int
        
        month = months.index(month) +1

        # filter by month to create the new dataframe
        df = df[df['month']==month]
   
    #filter by the day of week if applicable
    if day !='all':
        #filter by day of week to create the new dataframe
        df = df[df['day']==day.title()]
   
    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel.

    Args:
        (dataFrame)  df - data from city_data

    Returns:
        none
    """
    start_time = time.time()

    # display the most common month
    common_month = months[(df['month'].mode()[0])-1]
    print('The most common month for bicycle usage is ', common_month.capitalize())

    # display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day for bicycle usage is ', common_day)


    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(f"The most common hour for bicycle usage is hour {common_hour} ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (dataFrame)  df - data from city_data

    Returns:
        none
    """

    #print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used Start Station is:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used End Station is:', common_end_station)

    # display most frequent combination of start station and end station trip
    grouped = df.groupby(['Start Station', 'End Station']).size().idxmax()
   
    print('The most commonly used route is: ',grouped[0], "&", grouped[1])

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (dataFrame)  df - data from city_data

    Returns:
        none

    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Trip_Duration = df['Trip Duration'].sum()

    #Change seconds into minutes and seconds
    tot_mins, tot_secs = divmod(Trip_Duration, 60)

    #Change minutes and seconds into hours and minutes
    tot_hours, tot_mins = divmod(tot_mins, 60)
    # Print the result of total travel time in hours minutes and seconds
    print(f"The total travel time is: {tot_hours} hours, {tot_mins} minutes and {tot_secs} seconds",)

    # Caclulate the average travel dime
    average_travel_time = df['Trip Duration'].mean()

    #Find the minutes and secods of average travel time
    avg_mins, avg_secs = divmod(average_travel_time, 60)

    #Find the hours and minutes of the average travel time
    avg_hour, avg_mins = divmod(avg_mins, 60)

    #Print the result of the average travel time in hours, minutes and seconds
    print(F"The average travel time is {avg_hour} hour(s), {avg_mins} minutes and {avg_secs} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    
    Args:
        (dataFrame)  df - data from city_data

    Returns:
        none
        
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of each user type is: \n', user_types)

    # Display the counts of gender create an exception for the city of Washington

    if 'Gender' not in df.columns:
        print('The city of Washington does not include gender in its data.')
    else: print('The counts for each gender are: \n', df['Gender'].value_counts())

   
    # Display earliest, most recent, and most common year of birth

    #Earliest Birth Year
    if 'Birth Year' not in df.columns:
        print('The city of Washington does not include Birth Year in its data')

    else: print('The earliest user Birth Year is: \n',int(df['Birth Year'].min()))

    #Most Recent Birth Year
    if 'Birth Year' not in df.columns:
        print('The city of Washington does not include Birth Year in its data')

    else: print('The most recent user Birth Year is: \n',int(df['Birth Year'].max()))
  

      #Most Common Birth Year
    if 'Birth Year' not in df.columns:
        print('The city of Washington does not include Birth Year in its data')

    else: print('The most common user Birth Year is: \n',int(df['Birth Year'].mode()[0]))

   
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def chunk_data(df):
    """Displays 5 rows of data from the dataframe upon request of the user.
    
    Args:
        (dataFrame)  df - data from city_data

    Returns:
        none
        
    """
    start = 0
   
    while True:
        see_data = input('Would you like to see 5 lines of the raw data? Enter yes or no.')
        if see_data == 'yes':
            start+= 1
            print('5 lines of data:\n', df.iloc[(start-1)*5:start*5])
        elif see_data == 'no':
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        chunk_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

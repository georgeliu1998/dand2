## TODO: import all necessary packages and functions
import pandas as pd 


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    invalid_name = True
    while invalid_name:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n')
        if city.lower() in ('chicago', 'new york', 'washington'):
            invalid_name = False
        else:
            print('City name invalid! Please re-enter.')
    
    if city.lower() == 'chicago':
        return chicago
    elif city.lower() == 'new york':
        return new_york_city
    else:
        return washington


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Period name such as month, day or none
    '''
    invalid_time_period = True
    while invalid_time_period:
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
        if time_period.lower() in ('month', 'day', 'none'):
            invalid_time_period = False
        else:
            print('Time period invalid! Please re-enter.')

    if time_period == 'month':
        return 'month'
    elif time_period == 'day':
        return 'day'
    else:
        return 'none'


def get_month(city):
    '''Asks the user for a month and returns the specified month data as a df.

    Args:
        city.
    Returns:
        (pd df object) df 
    '''
    month = input('\nWhich month? Enter the month number such as 1 for Jannuary:\n')
    with open(city, 'r') as f_in:
        df=pd.read_csv(city)
        df['month'] = pd.to_datetime(df['Start Time']).dt.month
        df = df.query('month == @month')
    return df

def get_day(city):
    '''Asks the user for a day and returns the specified day.

    Args:
        city.
    Returns:
        (pd df object) df
    '''
    day = input('\nWhich day? Please type your response as an integer, 1 for Monday, 2 for Tuesday\n')
    with open(city, 'r') as f_in:
        df=pd.read_csv(city)
        df['day'] = pd.to_datetime(df['Start Time']).dt.dayofweek
        df = df.query('day == @day')
    return df


def popular_month(df):
    '''Finds the most popular month based on given city and time period
    Args:
        df
    Returns:
        (int) month number
    Question: What is the most popular month for start time?
    '''
    return pd.to_datetime(df['Start Time']).dt.month.value_counts().idxmax()


def popular_day(df):
    '''Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Args:
        df
    Returns:
        (int) day number
    '''
    return pd.to_datetime(df['Start Time']).dt.dayofweek.value_counts().idxmax()


def popular_hour(df):
    '''Question: What is the most popular hour of day for start time?
    Args:
        df
    Returns:
        (int) hour number
    '''
    # TODO: complete function


def trip_duration(df):
    '''Question: What is the total trip duration and average trip duration?
    Args:
        df
    Returns:
        (tuple) (total_duration, average_duration)
    '''
    total_duration = df['Trip Duration'].sum()
    average_duration = df['Trip Duration'].mean()
    return total_duration, average_duration


def popular_stations(df):
    '''Question: What is the most popular start station and most popular end station?
    Args:
        df
    Returns:
        (tuple of strings): start_station, end_station
    '''
    start_station = df['Start Station'].value_counts().idxmax()
    end_station = df['End Station'].value_counts().idxmax()
    return start_station, end_station

def popular_trip(df):
    '''Question: What is the most popular trip?
    Args:
        df:
    Returns:
        (string) trip
    '''
    return (df['Start Station']+'  TO  '+df['End Station']).value_counts().idxmax()
    

def users(df):
    '''Question: What are the counts of each user type?
    Args:
        df
    Returns:
        (pd.Series) counts
    '''
    return df['User Type'].value_counts()


def gender(df):
    '''Question: What are the counts of gender?
    Args:
        df
    Returns:
        (pd.Series) counts
    '''
    return df['Gender'].value_counts()


def birth_years(df):
    '''Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Args:
        df
    Retruns:
        (tuple) oldest, youngest, popular
    '''
    oldest = df['Birth Year'].min()
    youngest = df['Birth Year'].max()
    popular = df['Birth Year'].value_counts().idxmax()
    return oldest, youngest, popular



def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        df
    Returns:
        pandas df object
    '''
    
    invalid_input = True
    while invalid_input:
        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')
        if display.lower() in ('yes', 'no'):
            invalid_input = False
        else:
            print('Input invalid! Please re-enter.')

    if display == 'yes':
        print(df.head(5))

    count = 5
    display_contd = 'continue'
    while display_contd == 'continue':
        invalid_input = True
        while invalid_input:
            display_contd = input('\n\'continue\' or \'stop\'?\n')
            if display_contd.lower() in ('continue', 'stop'):
                invalid_input = False
                if display_contd == 'continue':
                    print(df[count:count+5])
                    count += 5
                else:
                    break
            else:
                print('Input invalid! Please re-enter.')


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the statistics...')

    # What is the most popular month for start time?
    if time_period == 'month':
        df = get_month(city)
    elif time_period == 'day':
        df = get_day(city)
    else:
        with open(city, 'r') as f_in:
            df=pd.read_csv(city)

    print('\nWhat is the most popular day of week (Monday, Tuesday, etc.) for start time?') 
    print(popular_day(df))

    print('\nWhat is the most popular hour of day for start time?')
    print(popular_hour(df)) 

    print('\nWhat is the total trip duration and average trip duration?')
    print(trip_duration(df))

    print('\nWhat is the most popular start station and most popular end station?')
    print(popular_stations(df))

    print('\nWhat is the most popular trip?')
    print(popular_trip(df)) 

    print('\nWhat are the counts of each user type?')
    print(users(df)) 

    print('\nWhat are the counts of gender?') 
    if city != 'washington.csv':
        print(gender(df))
    else:
        print('no gender info avaialbe in this dataset')

    print('\nWhat are the earliest (i.e. oldest user), most recent (i.e. youngest user), and/nmost popular birth years?') 
    if city != 'washington.csv':
        print(birth_years(df))
    else:
        print('no birth year info avaialbe in this dataset')

    # Display five lines of data at a time if user specifies that they would like to
    display_data(df)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
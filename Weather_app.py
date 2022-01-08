'''
Jeremy Johnson
CIS245
1/7/22
Weather Application
'''

import requests


# API Key add364ebb97cd91c8d024101440ce4bf for ease of use

# main function that handles the greeting and code flow for city and zip options. 

def Main():
   
    Greeting() # Calls the greeting function to greet user. 
 
    while True:
        userInput = input('Would you like to search by your City or your Zip Code? Please enter either *city* or *zip*: ')
        userInput = userInput.lower()

        if userInput == 'city':
            print('\nOne moment while I pull that up.\n')
            City()
        elif userInput == 'zip':
            print('\nOne moment while I pull that up.\n')
            Zip()      
        else:
            print('\nI\'m sorry I dont understand, please try again.\n')


def Greeting(): # Generic greeting message to greet the user. 

    print('Welcome to my new Weather Forecast Application. Please follow the prompts to see your forecast.\n')


def Loop(): # Loop function used to trigger the program to run again in full or to exit the program.

    choice = input('\nWould you like to look up another forecast? If so, please enter *yes*. If not, please enter *no*: ')
    choice = choice.lower()

    if choice == 'yes':
        print()
        Main()
    elif choice == 'no':
        print('\nGoodbye!')
        exit()
    else:
        print('That is not a valid answer, please try again.')


def City(): # Handles the API call if the City option is chosen in Main. Uses try blocks to give a pass/fail response.

    cityName = input('Please enter your City Name: ')
    cityName = cityName.lower()

    try:
        print('\nGetting your forecast ready!')
        link = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=add364ebb97cd91c8d024101440ce4bf&units=imperial'.format(cityName)
        req = requests.get(link)
        forecast = req.json()
        Weather(forecast)
        
    except:
        print('\n404 Client Error: Not Found URL. Please enter a valid City name.\n')
        City()

    Loop()


def Zip(): # Handles the API call if the Zip Code option is chosen in Main. Uses try blocks to give a pass/fail response.

    zipCode = input('Please enter your Zip Code: ')

    try:
        print('\nGetting your forecast ready!')
        link = ('https://api.openweathermap.org/data/2.5/weather?zip={},us&appid=add364ebb97cd91c8d024101440ce4bf&units=imperial'.format(zipCode))
        req = requests.get(link)
        forecast = req.json()
        Weather(forecast)
    except:
        print('\n404 Client Error: Not Found URL. Please enter a valid Zip Code.\n')
        Zip()

    Loop()


def Weather(forecast): # Retrieves, stores, formats and displays the json data from both City and Zip API calls.
    
    description = forecast['weather'][0]['description']
    temperature = forecast['main']['temp']
    tempfeel = forecast['main']['feels_like']
    tempmin = forecast['main']['temp_min']
    tempmax = forecast['main']['temp_max']
    name = forecast['name']
    windspeed = forecast['wind']['speed']
    winddir = forecast['wind']['deg']
    humidity = forecast['main']['humidity']

  # Rounding results into round numbers where necessary

    temperature = round(temperature)
    tempfeel = round(tempfeel)
    tempmin = round(tempmin)
    tempmax = round(tempmax)
    windspeed = round(windspeed)
   
   # If ladder that converts wind direction from degrees into human readable cardinal directions.

    if winddir >= 350 or winddir >=0 and winddir < 20:
        winddir = 'North'
    elif winddir >= 20 and winddir < 40:
        winddir = 'North North East'
    elif winddir >= 40 and winddir < 60:
        winddir = 'North East' 
    elif winddir >= 60 and winddir < 80:
        winddir = 'East North East'
    elif winddir >= 80 and winddir < 110:
        winddir = 'East'
    elif winddir >= 110 and winddir < 130:
        winddir = 'East South East' 
    elif winddir >= 130 and winddir < 150:
        winddir = 'South East'  
    elif winddir >= 150 and winddir < 170:
        winddir = 'South South East' 
    elif winddir >= 170 and winddir < 200:
        winddir = 'South'   
    elif winddir >= 200 and winddir < 220:
        winddir = 'South South West' 
    elif winddir >= 220 and winddir < 240:
        winddir = 'South West'  
    elif winddir >= 240 and winddir < 260:
        winddir = 'West South West' 
    elif winddir >= 260 and winddir < 290:
        winddir = 'West'   
    elif winddir >= 290 and winddir < 310:
        winddir = 'West North West' 
    elif winddir >= 310 and winddir < 330:
        winddir = 'North West'  
    elif winddir >= 330 and winddir < 350:
        winddir = 'North North West'

    #print(forecast) # for testing purposes and data validation.

    # the following print statements print the retrieved data into a format that is human readable.

    print('\nHere is today\'s forecast for {}.\n'.format(name)) 
    print('Today\'s forecast calls for {}.'.format(description))
    print('The current Temperature is {} degrees Fahrenheit.'.format(temperature))
    print('The humidity is {}%.'.format(humidity))
    print('The high for today is {} degrees Fahrenheit.'.format(tempmax))
    print('The low for today is {} degrees Fahrenheit.'.format(tempmin))
    print('The temperature feels like {} degrees Fahrenheit.'.format(tempfeel))
    print('The current wind speed is {} miles per hour from the {}.'.format(windspeed, winddir))
    
# start of the actual program

Main()
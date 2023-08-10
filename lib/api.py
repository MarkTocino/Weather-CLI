import requests
import argparse
import pyfiglet
from simple_chalk import chalk
BASE_URL = "http://api.weatherapi.com/v1/current.json?key=e984033b925f443ebc1211505230608"

no = f"{pyfiglet.figlet_format('GOODBYE')}\n\n"
def byebye():
    print(chalk.red(no))
    exit()


def fetch_weather():
    from functions import is_logged_in
    if is_logged_in == True: 
        from functions import units, humids, precips,feels, visibs
    global city
    try:
        city = input(chalk.green("Type a city here: "))
        url = f"{BASE_URL}&q={city}&aqi=no"

        response = requests.get(url)
        data = response.json()

        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        if is_logged_in:
            if units == "1" or units == "metric":
                temp = data["current"]["temp_c"]
            else:
                temp = data["current"]["temp_f"]
        else:
            temp = data["current"]["temp_f"]
        local_time = data["location"]["localtime"]
        if is_logged_in:
            if units == "1" or units == "metric":
                wind = data["current"]["wind_kph"]
            else:
                wind = data["current"]["wind_mph"]
        else:
            wind = data["current"]["wind_mph"]
        wind_dir = data["current"]["wind_dir"]
        if is_logged_in: 
            if precips == "1" and units == "1" or units == "metric":
                precip = data["location"]["precip_mm"]
            elif precips == "1" and units == "2" or units == "imperial":
                precip = data["location"]["precip_in"]
            elif precips == "1" and units == None:
                precip = data["location"]["precip_in"]
            else:
                pass
        else:
            pass
        if is_logged_in: 
            if humids == "1":
                humidity = data["location"]["humidity"]
            else:
                pass
        current_condition = data['current']['condition']["text"]
        if is_logged_in:
            if feels == "1" and units == "1" or units == "metric":
                feels_like = data['current']['feels_like_c']
            elif feels == "1" and units == "2" or units == "imperial":
                feels_like = data['current']['feels_like_f']
            elif feels == "1" and units == None:
                feels_like = data['current']['feels_like_f']
            else:
                pass
        else:
            pass
        if is_logged_in: 
            if visibs == "1" and units == "1" or units == "metric":
                vis = data['current']['vis_km']
            elif visibs == "1" and units == "2" or units == "imperial":
                vis = data['current']['vis_miles']
            elif visibs == "1" and units == None:
                vis = data['current']['vis_miles']
            else:
                pass
        else:
            pass
        

        output = f"{pyfiglet.figlet_format(location)}, {pyfiglet.figlet_format(region)},{pyfiglet.figlet_format(country)}\n\n"
        output += f"Temperature {temp}F\n\n"
        if is_logged_in:
            if feels is not None:
                output += f"Temperature feels like {feels_like}\n\n"
        output += f"Local Time {local_time}\n\n"
        output += f"Current Wind {wind}mph {wind_dir}\n\n"
        if is_logged_in:
            if precips is not None:
                output += f"Current Precipitation {precip}\n\n"
        if is_logged_in:        
            if humids is not None:
                output += f"Current Humidity {humidity}\n\n"
        if is_logged_in:
            if visibs is not None:
                output += f"Current visibility is {vis}\n\n"
        output += f"Current Condition {current_condition} : "

        if data:
            if data["current"]["condition"]["text"] == "Sunny":
                output += "☀️"
            elif data["current"]["condition"]["text"] == "Partly cloudy":
                output += "⛅"
            elif data["current"]["condition"]["text"] == "Cloudy":
                output += "☁"
            elif data["current"]["condition"]["text"] == "Overcast":
                output += "⛅"
            elif data["current"]["condition"]["text"] == "Mist":
                output += "⛆"
            elif data["current"]["condition"]["text"] == "Pathcy rain possible":
                output += "🌦"
            elif data["current"]["condition"]["text"] == "Patchy snow possible":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy sleet possible":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy freezing drizzle possible":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Thundery outbreaks possible":
                output += "🌩"
            elif data["current"]["condition"]["text"] == "Blowing snow":
                output += "🌬"
            elif data["current"]["condition"]["text"] == "Blizzard":
                output += "⛇"
            elif data["current"]["condition"]["text"] == "Fog":
                output += "☁"
            elif data["current"]["condition"]["text"] == "Freezing fog":
                output += "☁"
            elif data["current"]["condition"]["text"] == "Patchy light drizzle":
                output += "🌦"
            elif data["current"]["condition"]["text"] == "Light drizzle":
                output += "🌦"
            elif data["current"]["condition"]["text"] == "Freezing drizzle":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Heavy freezing drizzle":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Patchy light rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate rain at times":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Heavy rain at times":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Heavy rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light freezing rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate or heavy freezing rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light sleet":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate or heavy sleet":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Patchy light snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy moderate snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy heavy snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Heavy snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Ice pellets":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light rain shower":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate or heavy rain shower":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Torrential rain shower":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light sleet showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate or heavy sleet showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light snow showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate or heavy snow showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light showers of ice pellets":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate or heavy showers of ice pellets":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy light rain with thunder":
                output += "⛈"
            elif data["current"]["condition"]["text"] == "Moderate or heavy rain with thunder":
                output += "⛈"
            elif data["current"]["condition"]["text"] == "Patchy light snow with thunder":
                output += "⛈☃"
            elif data["current"]["condition"]["text"] == "Moderate or heavy snow with thunder":
                output += "⛈☃"
            elif data["current"]["condition"]["text"] == "Clear":
                output += "🌝"
        print(chalk.blue(output))

        if response.status_code == 200:
            good_response_code()
    except KeyError:
             print(chalk.red("Sorry, No information is available because you are illiterate. Try again after looking up how to spell. Thank You!"))
             fetch_weather()

def get_city_input():
    return input(chalk.green("Enter a city: "))

def show_main_menu():
    from functions import is_logged_in
    return input(chalk.green(f'Enter 1 to try again, 2 for main menu, {"3 save city, or 4 to quit"if is_logged_in == True else "or 3 to quit"}: \n'))

def bad_status_code():
    print(chalk.red("Sorry, No information is available because you are illiterate. Try again after looking up how to spell. Thank You!"))
    fetch_weather()

def store_city(city_name):
    from functions import is_logged_in, session, current_user
    from db.models import User, City
    
    if is_logged_in and current_user:
        user = session.query(User).filter(User.id == current_user.id).first()
        if user:
            new_city = City(name=city_name)
            user.cities.append(new_city)
            session.commit()
            print(f"{city_name} has been saved")
        else:
            print("User not found")
    else:
        print("Login to save city")

def process_choice(choice):
    from functions import menu, is_logged_in
    if choice == '1':
        fetch_weather()
    elif choice == '2':
        menu()
    elif choice == '3':
        if is_logged_in:
            store_city(city)
        else:
            byebye()
    elif choice == '4':
        if is_logged_in == True:
            byebye()
        else:
            print(chalk.red(f"Invalid choice. Please enter 1, 2, or 3. Or else I'm kicking you out >:("))


def good_response_code():
    from functions import is_logged_in
    while True:
        choice = show_main_menu()
        if choice in (f'1 , 2, {"3 , 4"if is_logged_in == True else "3" } \n'):
            process_choice(choice)
        else:
            print(chalk.red(f"Invalid choice. Please enter 1, 2, {'3 or 4' if is_logged_in == True else 'or 3'}. Or else I'm kicking you out >:(\n"))
        

if __name__ == "__main__":
    good_response_code()
    
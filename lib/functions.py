import sys, time
from api import fetch_weather, byebye
from db.models import User, WeatherPreference, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_chalk import chalk


Session = sessionmaker(bind=engine)
session = Session()

is_logged_in = False
current_user = None

units = None
visibs = None
humids = None
precips = None
feels = None

def menu():
    print(chalk.green("Please select a option: "))
    selection = input(chalk.green(f"1: Get weather  {'2: Preferances  3: My Cities  4: quit' if is_logged_in == True else '2: Login  3: quit'}  \n"))
    if selection == "1" or selection.lower() == "get weather":
        fetch_weather()
    elif selection =="2" or selection.lower() == {"preferances" if is_logged_in == True else "login"}:
        add_preference() if is_logged_in == True else login()
    elif selection == "3" or selection.lower() == "my cities" :
       my_cities() if is_logged_in ==True else byebye()
    elif selection == "4" or selection.lower() == "quit":
        byebye()
    else:
        print(chalk.red("Invalid input, type \"back\" to go back to main menu or \"exit\" to quit."))
        menu()

    
def login():
    global current_user
    users = session.query(User)
    selection = input(chalk.green("Please type your username to login or type \"new\" to create new user.\n"))
    if selection in [user.username for user in users]:
        print("login success!")
        global is_logged_in
        is_logged_in = True
        current_user = session.query(User).filter(User.username == selection).first()
        menu()
    elif selection.lower() == "new":
        print("Create new user")
        add_user()
    elif selection.lower() == "back":
        menu()
    elif selection.lower() == "exit" or selection.lower() == "quit":
        byebye()
    else:
        print(chalk.red("Invalid input, type \"back\" to go back to main menu or \"exit\" to quit."))
        login()

def my_cities():
    if is_logged_in and current_user:
        user = session.query(User).filter(User.id == current_user.id).first()
        if user:
            saved_cities = user.cities
            if saved_cities:
                print("Here are your saved cities:")
                for city in saved_cities:
                    print(city)
            else:
                print("No cities are saved")
        else:
            print("No User found")
    else:
        print("You have to be logged in to see the cities you have saved")


def add_user():
    global current_user
    new_username = input("Enter a new username: ")
    new_user = User(username=new_username)
    session.add(new_user)
    session.commit()
    global is_logged_in
    is_logged_in = True
    current_user = session.query(User).filter(User.username == new_username)
    print("login success!")
    menu()

def add_preference():
    global units
    global visibs
    global humids
    global precips
    global feels
    new_units = input(chalk.green("Pick Metric or Imperial(american): 1 or 2\n"))
    new_precips = input(chalk.green("Would you like to add precipitation? 1 Yes 2 No\n"))
    new_humids = input(chalk.green("Would you like to add humidity? 1 Yes 2 No\n"))
    new_feels_likes = input(chalk.green("Would you like to add feels like temperature? 1 Yes 2 No\n"))
    new_visibs = input(chalk.green("Would you like to add visibility range? 1 Yes 2 No\n"))
    units = WeatherPreference(preferred_units=new_units)
    precips = WeatherPreference(precip_unit = new_precips)
    humids = WeatherPreference(humid_unit = new_humids)
    feels = WeatherPreference(feels_like_unit = new_feels_likes)
    visibs = WeatherPreference(visibility_unit = new_visibs)
    session.add(units)
    session.add(humids)
    session.add(visibs)
    session.add(precips)
    session.add(feels)
    session.commit()
    session.close()
    menu()

def use_preference(session):
    pass
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)

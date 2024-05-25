#LIBRARIES
import json
import sys

#REQUESTS
import requests
URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name"

#REQUEST
def requisition(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except:
        print("Request Error:", url)

#PARSE
def parsing(reponse_text):
    try:
        return json.loads(reponse_text)
    except:
        print("Parsing Error")

#COUNTING COUNTRIES
def count_countries():
    response = requisition(URL_ALL)
    if response:
        list_countries = parsing(response)
        if list_countries:
            return len(list_countries)

#LISTING COUNTRIES
def country_list(list_countries):
    for country in list_countries:
        print(country['name'])

#SHOWING POPULATION
def show_population(country_name):
    response = requisition("{}/{}".format(URL_NAME, country_name))
    if response:
        list_countries = parsing(response)
        if list_countries:
            for country in list_countries:
                print("{}: {} people".format(country['name'], country['population']))
    else:
        print("Country not found, please try again...")

#SHOWING CURRENCIES
def show_currencies(country_name):
    response = requisition("{}/{}".format(URL_NAME, country_name))
    if response:
        list_countries = parsing(response)
        if list_countries:
            for country in list_countries:
                print("Currencies", country['name'])
                currencies = country['currencies']
                for currency in currencies:
                    print("{} - {}".format(currency['name'], currency['code']))
    else:
        print("Country not found, please try again...")

#READING COUNTRIES NAMES
def read_country_name():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print("Enter country name")

#MAIN MENU
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("## Welcome to our API Country INFO 2.0 ##")
        print("Instructions: python countries.py <action> <country name>")
        print("Actions: counting, currency, population")
    else:
        argument1 = sys.argv[1]

        if argument1 == "counting":
            countries_number = count_countries()
            print("There are {} in the world!".format(countries_number))
        elif argument1 == "currency":
            country = read_country_name()
            if country:
                show_currencies(country)
        elif argument1 == "population":
            country = read_country_name()
            if country:
                show_population(country)
        else:
            print("Invalid argument, please try again...")

from csv import DictReader
from random import choice


def main():
    trivia_data = fetch_data()
    print(trivia_data)
    random_country = choice(trivia_data)
    country_keys = random_country.keys()
    attri = choice(list(country_keys)[1:])
    print(attri)

    african_countries = countries_filter(attri, 'Africa', trivia_data)
    print(len(african_countries))
    for _ in african_countries:
        print(f"{_['Country Name']} - {_['Capital']}")


def fetch_data():
    with open('countrycode.csv') as file:
        countries_data=(list(DictReader(file)))

    trivia_data = [{
        'Country Name': country['Country Name'],
        'Top Level Domain': country['Top Level Domain'],
        'Capital': country['Capital'],
        'Continent': country['Continent'],
        'Currency': country['Currency'],
        'Language Codes': country['Language Codes'],
        'Languages': country['Languages'],
        'Area KM2': country['Area KM2'],
        'Phones (Mobile)': country['Phones (Mobile)'],
        'Phones (Landline)': country['Phones (Landline)'],
                    } for country in countries_data]
    
    return trivia_data


def fetch_input(desc):
    return input(desc).strip()


def countries_filter(desc1, desc2, countries):
    return [country for country in countries if country[desc1] == desc2]


def initialize_logic():
    ...


main()
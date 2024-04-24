from csv import DictReader
from random import choice


def main():
    trivia_data, countries_data = fetch_data()
    num_of_questions = number_of_questions()
    user_choice = options_choosing(list(choice(trivia_data).keys())[1:])
    random_country = choice(countries_data)

    for _ in range(num_of_questions):
        user_answer = ask_user_question(random_country, user_choice)


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
    
    return trivia_data, countries_data


def ask_user_question(random_country, option):
    return input(f'WHAT IS THE {option.upper()} OF {random_country[option].upper()}: ')


def options_choosing(options):
    num = 1
    print('CHOOSE THE GAME FROM THE OPTIONS LISTED.')
    for option in options:
        print(f"{num}. {option.upper()}")
        num+=1
    user_choice = int(fetch_input('\nWHAT IS YOUR CHOICE: '))

    return options[user_choice-1]


def fetch_input(desc):
    return input(desc).strip()


def number_of_questions():
    return int(fetch_input('HOW MANY QUESTIONS DO YOU WANT TO ANSWER? '))


def countries_filter(desc1, desc2, countries):
    return [country for country in countries if country[desc1] == desc2]


main()
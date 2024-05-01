from csv import DictReader
from random import choice
from time import sleep


def main():
    game_is_on = True
    num_of_questions_asked = 0
    game_score=0
    trivia_data, countries_data = fetch_data()
    num_of_questions = number_of_questions()
    user_choice = options_choosing(list(choice(trivia_data).keys())[1:])
    
    while game_is_on:
        if num_of_questions_asked == num_of_questions:
            game_is_on = False
        else:
            hundred_dashes()
            random_country = choice(countries_data)
            print(display_info('Correctly answered : ', num=game_score))
            hundred_dashes()
            answer, user_answer = ask_user_question(random_country, user_choice)
            print(display_info('THE ANSWER IS : ', answer))
            for _ in range(3):
                print()
            if user_answer.lower == answer:
                game_score += 1
            
            num_of_questions_asked +=1



def display_info(info, desc='', num=''):
    return f"{info.upper()} {desc.upper()} {num}"


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
    # print(random_country)
    answer = random_country[option].lower()
    question_statement = question_sentence_generator(option, random_country['Country Name'])
    return answer, fetch_input(question_statement)


def options_choosing(options):
    num = 1
    print('CHOOSE THE GAME FROM THE OPTIONS LISTED.')
    for option in options:
        print(f"{num}. {option.upper()}")
        num+=1
    user_choice = int(fetch_input('\nWHAT IS YOUR CHOICE: '))

    return options[user_choice-1]

def hundred_dashes():
    print('-'*50)

def fetch_input(desc):
    return input(desc.upper()).strip()


def number_of_questions():
    return int(fetch_input('HOW MANY QUESTIONS DO YOU WANT TO ANSWER? '))


def countries_filter(desc1, desc2, countries):
    return [country for country in countries if country[desc1] == desc2]


def question_sentence_generator(specific_case, country_name):
    match specific_case:
        case 'Top Level Domain':
            return f"What is the {specific_case} of  {country_name} : ".upper()
        case 'Capital':
            return f"What is the {specific_case} of  {country_name} : ".upper()
        case 'Continent':
            return f"Which {specific_case} is {country_name} in : ".upper()
        case 'Currency':
            return f"What is the {specific_case} used in  {country_name} : ".upper()
        case 'Languages':
            return f"List the {specific_case} spoken in {country_name} : ".upper()
        case 'Language Codes':
            return f"How many {specific_case[0:8]}s are spoken in {country_name} : ".upper()
        case 'Area KM2':
            return f"What is the {specific_case[0:4]} of  {country_name} in square KM : ".upper()
        case 'Phones (Mobile)':
            return f"What is the {specific_case[9:-1]} specific code of the country {country_name} : ".upper()
        case 'Phones (Landline)':
            return f"What is the {specific_case[9:-1]} {specific_case[0:5]} code for  {country_name} : ".upper()        
        case _:
            return 'Unknown'

main()
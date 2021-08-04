
import random
import string
import os

settings = { 
    'lower': True , 
    'upper': True ,
    'symbol': True ,
    'number': True ,
    'space' : False ,
    'length': 8 
}

PASSWORD_MAX_LEN = 10
PASSWORD_MIN_LEN = 4

def clear_screen ():
    os.system('cls')


def get_user_password_lengh(option ,defaulte , ps_min_length = PASSWORD_MIN_LEN , ps_max_length = PASSWORD_MAX_LEN):
    while True:
        input_user = input('enter password length (Defalut is'
        f' {defaulte}) the ( enter: defaulte):' )

        if input_user == '':
            return defaulte

        if input_user.isdigit():
            password_lenth = int(input_user)

            if ps_min_length <= password_lenth <= ps_max_length :
                return password_lenth
            
            else:
                print('invalid number input.' 
                f'the number input should between {ps_min_length} and {ps_max_length}')
        else:
            print('invalid input. enter the number.')

        print('please try again.')
        


def get_yes_or_no_for_settinds(option , defaulte):
    while True:
        input_user = input(f'include {option}? (Defalut is {defaulte})' 
                            'the (y : yes , n : no , enter: defaulte):' )

        if input_user == '':
            return defaulte
        if input_user in ['y' , 'n']:
            return input_user == 'y'

        print('invali input. please try again.')



def get_sttings_from_user(settings):
    for option , defaulte in settings.items():
        if option != 'length':
            user_choice  = get_yes_or_no_for_settinds(option , defaulte)
            settings[option] = user_choice

        else:
            user_password_lengh = get_user_password_lengh(option ,defaulte)
            settings[option]= user_password_lengh
            

def ask_and_change_settings(settings):
    while True:
        user_answer = input('Do you want to change defaulte settings '
        ', (y : yes , n: no , enter:yes): ')

        if user_answer in ['y','n','']:
            if user_answer in ['y','']:
                print('-'*5 , 'change settings' , '-'*5 , sep='')
                get_sttings_from_user(settings)
            break
        
        else:
            print('invalid input.')
            print('try again.')



def get_random_upper_case():
   return random.choice(string.ascii_uppercase)

def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_symbol_case():
   return random.choice('!@#$%&*()?:')

def get_random_number_case():
   return random.choice(string.digits)



def generator_random_char(choices):

    select = random.choice(choices)

    if select == 'upper':
        return get_random_upper_case()

    if select == 'lower':
        return get_random_lower_case()

    if select == 'symbol':
        return get_random_symbol_case()

    if select == 'number':
        return get_random_number_case()

    if select == 'space':
        return ' '


def password_generator(settings):


    password_length = settings['length']
    final_password = ''
    choices = (list(filter(lambda x:settings[x] , ['lower','upper','symbol','number','space'])))

    
    for i in range(password_length):
        final_password += generator_random_char(choices)

    return final_password


def password_generator_again():
    while True:
        print('-'*20)
        print(f'password generator: {password_generator(settings)}')

        while True:
            want_password_generator = input('Do you want another password?:(y : yes , n: no , enter:yes)')
            if want_password_generator in ["y" , 'n' , '']:
                if want_password_generator == 'n':
                    return
                break

            else:
                print('invalid input.(choice from: y:yes , n:no , enter:yes)')
                print('please try again.')

def run ():
    clear_screen()
    ask_and_change_settings(settings)
    password_generator_again()
    print('Thank you for choosing us.')
    
run()
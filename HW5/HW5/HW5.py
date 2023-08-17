# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.

def my_converter(arg):
    try:
        return float(arg)

    except ValueError:
        print ('valueerror')
        return 0

    except TypeError:
        print ('typeerror')
        return 0

    except NameError:
        print ('nameerror')
        return 0

    except Exception:
        print ('wrong !')
        return 0
    
print (my_converter(input("enter the nomber :")))

# 2. Напишіть функцію, що приймає два аргументи. Функція повинна a. якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів, b. якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути c. у будь-якому іншому випадку повернути кортеж з цих аргументів

def my_calculator(first, second):
    try:
        if isinstance(first, (int, float)) and isinstance(second, (int, float)):
            return first * second
        elif isinstance(first, str) and isinstance(second, str):
            return first + second
        else:
            return (first, second)
    except Exception:
        print ('wrong !')
        return 0

user_input1 = input("enter something: ")
user_input2 = input("enter another value: ")

try:
    user_input1_float = float(user_input1)
except ValueError:
    user_input1_float = user_input1

try:
    user_input2_float = float(user_input2)
except ValueError:
    user_input2_float = user_input2

result = my_calculator(user_input1_float, user_input2_float)
print (result)

# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне: a. Попросіть користувача ввести свсвій вік. i. - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?" ii. - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!" iii. - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!" iv. - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить" v. - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!" b. Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...). Наприклад : "Тобі ж 5 років! Де твої батьки?" "Вам 81 рік? Покажіть пенсійне посвідчення!" "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"
 
def generate_message(user_input, declination):
    if '7' in str(user_input):
        return f"вам {user_input} {declination}, вам пощастить"
    elif user_input < 7:
        return f"тобі ж {user_input} {declination}! де твої батьки?"
    elif 6 <= user_input < 16:
        return f"тобі лише {user_input} {declination}, а це е фільм для дорослих!"
    elif user_input > 65:
        return f"вам {user_input} {declination}? покажіть пенсійне посвідчення!"
    else:
        return f"незважаючи на те, що вам {user_input} {declination}, білетів всеодно нема!"

def cinema_cashier():
    max_attempts = 3
    attempts = 0

    while True:
        user_input = input('enter your real age: ')
        if user_input.isdigit():
            user_input = int(user_input)
        if 3 <= user_input <= 122:
            break
        else:
            print ('wrong! Enter the number!')
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print (f"remaining attempts: {remaining_attempts}")
            if attempts == max_attempts:
                print ("exceeded maximum attempts")
                exit()

    def get_age_declination(user_input):
        if user_input % 10 == 1 and user_input != 11:
            declination = " рік "
        elif 2 <= user_input % 10 <= 4 and (user_input < 10 or user_input > 20):
            declination = " роки "
        else:
            declination = " років "
        return declination

    declination = get_age_declination(user_input)
    message = generate_message(user_input, declination)
    
    return message

print (cinema_cashier())

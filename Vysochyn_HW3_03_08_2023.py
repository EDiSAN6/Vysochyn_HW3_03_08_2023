# 1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".

while True:
    user_input = input('enter word: ')
    if user_input.isdigit():
        print ("enter a word not a number! ")
    else:
        break

res = len(user_input)

while True:
    try:
        value = int(input('enter the character number in the word: '))
    except ValueError:
        print ('it\'s not a number!')
    except Exception:
        print ('wrong!')
    else:
        if value > res or value < 0:
            print ("enter the character number in the word!")
        else:
            print ('good choice!')
            break

message = f"The {value} symbol in '{user_input}' is '{user_input[value]}'"
print (message)

# 2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.

while True:
    user_input = input('enter a line with the words: ')
    if user_input.isdigit():
        print ("enter a word not a number! ")
    else:
        break

words = user_input.split()

num_words = len(words)

print (f"number of words per line: {num_words}")

# 3. Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

def extract_numbers(lst):
    return [x for x in lst if isinstance(x, (int, float))]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = extract_numbers(lst1)
print (lst2)

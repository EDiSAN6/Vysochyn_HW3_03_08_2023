# 1 Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.

print ("first task:")

while True:
    user_input = input('write a proposal: ')
    if user_input.isdigit():
        print ("no need to write numbers here! ")
    else:
        break

vowels = "AEIOUYaeiouy"

words = user_input.split()

count_words_with_double_vowels = 0

for word in words:
    for double_vowels in range(len(word)):
        if word[double_vowels] in vowels and word[double_vowels+1] in vowels:
            count_words_with_double_vowels += 1
            break  

print (count_words_with_double_vowels)

# 2 Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
 
print ("second task:")

dict = { "cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
min = 37.166
max = 49.999
            
for dict_key, dict_value in dict.items():
    if min < dict_value < max :
        print (dict_key)

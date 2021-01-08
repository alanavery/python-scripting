# Write to a file, method 1 ——————————————————————————————
hello_file = open('hello.txt', 'w')
ga_intro = 'Hello to all my friends at GA!'
hello_file.write(ga_intro)
# print(hello_file.read())
hello_file.close()

city_file = open('city.txt', 'w')
new_cities = '''Seattle
Portland
Baltimore
Miami
St. Louis'''
city_file.write(new_cities)
# print(city_file.read())
city_file.close()

my_new_file = open('profile.txt', 'w')
my_new_file.write('Alan Avery')
my_new_file.close()

# person_file = open('profile.txt')
# print(person_file.read())
# person_file.close()

# Write to a file, method 2 ——————————————————————————————
# with open('profile.txt', 'w') as person_file:
#     person_file.write('Brooke Ward\n')

# with open('profile.txt', 'a') as person_file:
#     person_file.write('Walter Mansilla\n')

# with open('profile.txt', 'a') as person_file:
#     person_file.write('Amanda O\'Neil\n')

# with open('profile.txt', 'r+') as person_file:
#     print(person_file.read())
#     person_file.write('Alan Avery')

# with open('profile.txt') as people:
#     people_list = people.readlines()
#     print(people_list)

# for each_person in people_list:
#     print(each_person)


def multiply_by_2(file):
    with open(file, 'r+') as num_digits:
        num_digits_list = num_digits.readlines()
        for each_num in num_digits_list:
            product = int(each_num) * 2
            print(product)


multiply_by_2('prime-numbers.txt')


def five_or_fifteen(file):
    solution = []
    with open(file, 'r+') as num_text:
        num_text_list = num_text.readlines()
        for each_num in num_text_list:
            if 'Five' in each_num or 'Fifteen' in each_num:
                solution.append(each_num.replace('\n', ''))
    print(solution)


five_or_fifteen('five-or-fifteen.txt')

# text_lst = hello_file.read().split(' ')

#.capitalize(), .title(), .center(), .ljust(), .rjust(), .zfill(),
# .format(), .format_map(), .swapcase(), .upper(), .lower()
string = "hello world"
print(string.capitalize())
print(string.upper())
print(string.title())
print(string.zfill(20))

second_string = "python"
character = "*"
print(second_string.center(20, character))

print("The price is {price} dollars".format(price = 22))


names = ["Adair", "Dhayana", "Christian", "Monserrat"]

for name in names:
    char = "*"
    justified = name.ljust(20, char)
    print(justified)

test = "this IS a tEsT"
capitalized_text = test.capitalize()
print(capitalized_text.swapcase())


"""
leaderboard = {"Adair": 100, "Dhayana": 95, "Christian": 80, "Monserrat": 35}

for index, data in enumerate(leaderboard.items()):
    char = "*"
    str_index = str(index)
    str_data = str(data)
    print(str_index)
    print(str_data)
    name, score = data
    print(name, score)
    for name, score in data:
        name, score = data
        justified_name = name.ljust(20, char)
        justified_score = name.rjust(20, char)
        print(justified_name, justified_score)"""

"""
    left_text = name.ljust(20, char)
    right_text = score.rjust(20, char)
    print(left_text, right_text)"""


#.count(), .find(), .index(), .rfind(), .rindex(), .startswith(), .endswith()
counting = "experience"
print(counting.count("e"))


def validate_pdf(file):
    if file.startswith("re") and file.endswith("pdf"):
        print("It's a valid PDF")
    else:
        print("Check your file")

passed_file = "report.pdf"
validate_pdf(passed_file)


sentence = "The catalog has a cat and a caterpillar"
print(sentence.find(" cat "))
print(sentence.rfind("a"))


def counting_words(sentence, word_):
    word_validated = 0

    for word in sentence:
        if word_ in sentence:
            word_validated += 1
            print("The word {word} appears at least two times.")

validate_sentence = "The cat is a cat and also a cat"
counting_words(validate_sentence, "cat")

print("Python3".isalnum())

validation = "123"
if validation.isdigit:
    print("Is digit")
elif validation.isdecimal():
    print("is decimal")
elif validation.isalnum():
    print("Is alphanumeric")
else:
    print("I don't know the type")

def validate_identifier(identifier):
    if identifier.isidentifier():
        print(f"The string {identifier} is a valid identifier")
    else:
        print(f"The string {identifier} is not a valid identifier")

test_identifier = "2hola_python"
validate_identifier(test_identifier)


def check_printable(string):
    if string.isprintable():
        print(f"The string {string} is printable")
    else:
        print("The string is not printable")

test_string = "Hello"
check_printable(test_string)


string = " hello world "
print(string.strip())

python = "I love Python"
print(python.replace("Python", "Java"))

list = "one,two,three"
splitted_list = list.split(",")
print(splitted_list)
print("|".join(splitted_list))

remove_rarities = "unlocking"
without_prefix = remove_rarities.removeprefix("un")
without_suffix = without_prefix.removesuffix("ing")
print(without_suffix)

names.sort(reverse=True)
print(names)

sorted_names = sorted(names)
print(sorted_names)
print(names)
import string

def remove_punctuation(phrase):
    cleaned_text = phrase.translate(str.maketrans("", "", string.punctuation)).lower()
    return cleaned_text

print(remove_punctuation("Hola!, Adair?"))
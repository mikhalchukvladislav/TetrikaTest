from AnimalsDict import animals_adding
import requests
import bs4


def main():
    url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

    animals_list = []
    animals_dict = {}
    animals_adding(animals_dict, url)

    for letter, value in animals_dict.items():
        print(str(letter) + ': ' + str(len(value)))


if __name__ == "__main__":
    main()
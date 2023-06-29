from search_feature import options
from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE


BASE_URL = "https://gateway.marvel.com:443/v1/public/"
URL = 'https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=ju&apikey=65b63a958c2733164ab372a2d69e038b'

# initialize marvel API
marvel_data = Marvel(MARVEL_PUBLIC, MARVEL_PRIVATE)

character_data = marvel_data.characters


def get_character_json(character_name):
    return character_data.all(name=character_name)


def main():
    print("Welcome to Hero Search!")
    options()


if __name__ == "__main__":
    main()
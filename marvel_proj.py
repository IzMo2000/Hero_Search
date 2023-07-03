from search_feature import options

BASE_URL = "https://gateway.marvel.com:443/v1/public/"
URL = 'https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=ju&apikey=65b63a958c2733164ab372a2d69e038b'



def main():
    print("Welcome to Hero Search!")
    options()


if __name__ == "__main__":
    main()
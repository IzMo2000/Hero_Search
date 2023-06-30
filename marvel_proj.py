from search_feature import options
from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE

# initialize marvel API
marvel_data = Marvel(MARVEL_PUBLIC, MARVEL_PRIVATE)

character_data = marvel_data.characters


# Title: Get Character JSON
# Description: Retrieves the JSON data for a specific character
#              from a data source.
# Input: character_name (str) - The name of the character
#        to search for.
# Output / Returned: JSON data representing the character.
# Output / Display: None
def get_character_json(character_name):
    return character_data.all(name=character_name)


def main():
    print("Welcome to Hero Search!")
    options()


if __name__ == "__main__":
    main()

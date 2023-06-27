# Welcome to Hero Search

## Setup Instructions
Hero Search utilizies the following libraries:
* [marvel](https://pypi.org/project/marvel/) - interfaces with Marvel API to obtain data
* [pandas](https://pandas.pydata.org/docs/getting_started/install.html) - converts json dictionary to readable dataframe
* [sqlalchemy](https://pypi.org/project/SQLAlchemy/) - enables data engine

# How to Run
Hero Search is a command line program. You can run Hero Search by entering the following in the command line

```python3 [directory]hero_search.py```

"[directory]" is the file directory containing the program files. If you are currently in the directory, just ```hero_search.py``` may be used.

# Overview
This program searches for and displays information for a given Marvel Hero using the official [Marvel API](https://developer.marvel.com/).

It will prompt the user for a hero's name to be entered, then display a short description of the Hero, along with a sample of some of the comics they've
been in and their total appearances amongst different Marvel comic series.
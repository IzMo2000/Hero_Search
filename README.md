# Welcome to Hero Search

## Setup Instructions
Hero Search utilizies the following libraries:
* [marvel](https://pypi.org/project/marvel/) - interfaces with Marvel API to obtain data
* [pandas](https://pandas.pydata.org/docs/getting_started/install.html) - enables database operations in python
* [sqlite3](https://www.sqlite.org/index.html) - enables data engine

# How to Run
Hero Search is a command line program. You can run Hero Search by entering the following in the command line

```python3 [directory]hero_search.py```

"[directory]" is the file directory containing the program files. If you are currently in the directory, just ```hero_search.py``` may be used.

# Overview
This program searches for and displays information for a given Marvel character using the official [Marvel API](https://developer.marvel.com/)

This program can search and store data for marvel characters using the api described above.

The following character data is displayed upon search:

* Name
* Description (if available)
* Number of character's appearances in
    * comics
    * series
    * stories
    * events

And is then stored in a history database (appears as hero_data.db in the program's local directory)

The history database can then be accessed from the main menu, where past search data can be reacquired and displayed.

# Automated Tests
![Style Check](https://github.com/IzMo2000/Hero_Search/actions/workflows/style_check.yaml/badge.svg)
![Unit Test](https://github.com/IzMo2000/Hero_Search/actions/workflows/unit_test.yaml/badge.svg)

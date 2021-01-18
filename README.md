# carols-plants

An image repository for the Shopify Summer 2021 Backend Developer Intern Challenge with search functions. The concept behind this application is based on a store that sells BC native plants.

This project is written in Python using Flask as the web framework and SQLite for the database engine.

## Usage
This web app has been deployed to Heroku: https://carols-plants.herokuapp.com

### Or run the app yourself:
#### 1. Install the dependencies
```
pip3 install -r requirements.txt
```
#### 2. Run the app
```
python3 app.py
```
#### 3. Visit http://127.0.0.1:5000/

## Possible Future Implementations
Given more time, there are a few features I would have liked to include.

First, I would optimize the search ability to still give results to misspelled words, such as somebody trying to type "apple", but wrote "aple" instead. I would implement this using regular expressions to search against the database.

Second, I would add a feature for users to input their own image of a plant to find similar looking plants in my database. To implement this, I might integrate Google's Cloud Vision API. Through my brief read through their documentation, it seems that the Image Properties feature would be helpful in detecting plants with similar coloured flowers that aren't green, since most of the plant images in my database are predominantly green.

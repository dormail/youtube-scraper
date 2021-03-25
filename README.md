# youtube-scraper
A python script scraping data about a youtube video

## Required packages
- For opening a .xls file pandas needs xlrd and openpyxl, though
it currently uses the .ods file format

## Usage
Before the script can be used a valid API Key has to be saved in `secret.py`.

The program can be used by typing
`python run.py <Filename>` 
and creates a file named `vidinfo-<Filename>` with all the necessary
columns.

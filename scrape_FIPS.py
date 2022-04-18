# get FIPS codes into df 

# libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml

def scrape_FIPS(url = 'https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code'):
    '''get FIPS code, scraping table from wikipedia 
    returns dataframe of name, alpha code, numeric code 
    via US FIPS designation'''

    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'lxml')
    # get code from inspecting page element
    table1 = soup.find('table')

    # # get header names
    # cols = []
    # for id in table1.find_all('th'):
    #     col = id.text
    #     cols.append(col)


    # Create a pandas df for scraped fips data, and columns
    fips = pd.DataFrame(columns = ['NAME', 'Alpha_code', 'STATE', 'Delete'])

    # Loop and fill in rows 
    for i in table1.find_all('tr')[1:]:
        row_vals = i.find_all('td')
        row = [val.text for val in row_vals]
        size = len(fips)
        fips.loc[size] = row

    # get rid of extra column
    fips.drop('Delete', inplace=True, axis=1)
    fips.drop('STATE', inplace=True, axis=1)
    return fips

# working script, visualizing data on US map
ipython



## import libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup
import re
import lxml

# load df
# df = pd.read_csv("data/NST-EST2021-alldata.csv") # all data
# df = pd.read_csv("data/NST-EST2021-popchg2020_2021.csv") # just population change


# get fips codes
def scrape_FIPS(url = 'https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code'):
    '''get FIPS code, scraping table from wikipedia 
    returns dataframe of name, alpha code, numeric code 
    via US FIPS designation'''

    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'lxml')
    # get code from inspecting page element
    table1 = soup.find('table')

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

 # update and join df
# data = pd.merge(fips, df, on='NAME')

def map_usa(data, var):
    '''data frame with FIPS code (data)
    var: variable to visualize
    returns: map of USA with heatmap visualized'''
    fig = px.choropleth(data,  # Input Pandas DataFrame
                        locations="Alpha_code",  # DataFrame column with locations
                        color="var",  # DataFrame column with color values
                        hover_name="NAME", # DataFrame column hover info
                        locationmode = 'USA-states') # Set to plot as US States
    fig.update_layout(
        title_text = 'National ranking - numeric change in resident total population 7/1/2020 to 7/1/2021 ', # Create a Title
        geo_scope='usa',  # Plot only the USA instead of globe
    )
    fig.show()  # Output the plot to the screen

# just look at certain states 
fig = px.choropleth(locations=["CA", "TX", "NY"], locationmode="USA-states", color=[1,2,3], scope="usa")
fig.show()


# custom US map using plotly graph objects
fig = go.Figure(data=go.Choropleth(
    locations=data['Alpha_code'], # Spatial coordinates
    z = data['POPESTIMATE2021'], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "2021 Population",
))

fig.update_layout(
    title_text = 'Population estimate as of 7/1/2021',
    geo_scope='usa', # limite map scope to USA
)
fig.show()
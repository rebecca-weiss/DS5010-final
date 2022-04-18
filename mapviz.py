# working script, visualizing data on US map
ipython
## import libraries
import pandas as pd
import plotly.express as px
import scrape_FIPS

# load df
# df = pd.read_csv("data/NST-EST2021-alldata.csv") # all data
df = pd.read_csv("data/NST-EST2021-popchg2020_2021.csv") # just population change
# states = df[['STATE', 'NAME']]

# get fips codes
fips = scrape_FIPS.scrape_FIPS()
 # update and join df
data = pd.merge(fips, df, on='NAME')


fig = px.choropleth(data,  # Input Pandas DataFrame
                    locations="Alpha_code",  # DataFrame column with locations
                    color="NRANK_NPCHG2021",  # DataFrame column with color values
                    hover_name="NAME", # DataFrame column hover info
                    locationmode = 'USA-states') # Set to plot as US States
fig.update_layout(
    title_text = 'National ranking - numeric change in resident total population 7/1/2020 to 7/1/2021 ', # Create a Title
    geo_scope='usa',  # Plot only the USA instead of globe
)
fig.show()  # Output the plot to the screen

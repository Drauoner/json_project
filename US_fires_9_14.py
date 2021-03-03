# Use the files below to compare the fires that have been burning in California between Sept 1-13 and Sept 14 - 20. 
# This file contains information about the latitude and longitude, and the brightness of each fire. 
# Using what you have learnt in processing a JSON files and mapping, make a map that shows the fires. 
# You will need separate programs to represent each JSON file. One file is from 9-1-20 to 9-13-20 
# and the other is from 9-14-20 to 9-20-20. 
# We are only interested in fires that have a brightness factor above 450.

import json

infile = open('US_fires_9_14.json','r')
outfile = open('readable_US_Fires_9_14.json','w')


# The json.load() function converts the data into a format Python 
# can work with: in this case, a giant dictionary

fire_data = json.load(infile)

#Formats data to make it more readable

#json.dump(fire_data,outfile,indent=4)

#print(eq_data.get("features")[0].get("properties").get("mag"))
#print(eq_data['features'][0]["properties"]["mag"])

list_of_fires = [i for i in fire_data]

brights, lons, lats = [],[],[]

for fire in list_of_fires:
    bright = fire['brightness']
    lon = fire['longitude']
    lat = fire['latitude']
    if bright>450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
#    'text':hover_texts,
    'marker':{
        'size':[bright/30 for bright in brights],
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }


}]

my_layout = Layout(title='US Fires - 9/14/2020 through 9/20/2020')

fig = {'data':data,'layout':my_layout}

offline.plot(fig, filename='US_Fires_9_14.html')


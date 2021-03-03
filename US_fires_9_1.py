# Use the files below to compare the fires that have been burning in California between Sept 1-13 and Sept 14 - 20. 
# This file contains information about the latitude and longitude, and the brightness of each fire. 
# Using what you have learnt in processing a JSON files and mapping, make a map that shows the fires. 
# You will need separate programs to represent each JSON file. One file is from 9-1-20 to 9-13-20 
# and the other is from 9-14-20 to 9-20-20. 
# We are only interested in fires that have a brightness factor above 450.

import json

infile = open('US_fires_9_1.json','r')
outfile = open('readable_US_Fires_9_1.json','w')


# The json.load() function converts the data into a format Python 
# can work with: in this case, a giant dictionary

fire_data = json.load(infile)

#Formats data to make it more readable

json.dump(fire_data,outfile,indent=4)

#print(eq_data.get("features")[0].get("properties").get("mag"))
#print(eq_data['features'][0]["properties"]["mag"])

list_of_fires = fire_data[]

brights, lons, lats, = [],[],[]

for fire in list_of_fires:
    bright = fire['properties']['mag']
    lon = fire['longitude']
    lat = fire['latitude']

    hover_texts.append(hover_text)
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }


}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data,'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')
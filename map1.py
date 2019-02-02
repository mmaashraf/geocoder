import folium
import pandas
#import webcolors
#function which decide the color of the markers
def getcolor(height):
    if 0<height<=1300:
        return 'orange'
    elif 1300<height<=2600:
        return 'blue'
    else:
        return 'red'

#creating a map object
map1=folium.Map(location=[36,-120],tiles="Mapbox Bright",zoom_start=10)

#extract lat and long data to add markers
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
info_height=list(data["ELEV"])
#adding marker
#adding children to a fearure group
fg=folium.FeatureGroup(name="feat_map1")
fgp = folium.FeatureGroup(name="Population")



#polygon layer and population layer
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#marker layer
#circle marker layer
for lt,lo,pop_up in zip(lat,lon,info_height):
    fg.add_child(folium.Circle(location=[lt,lo],popup=str(pop_up)+" m",fill=True,color=getcolor(pop_up),fill_color=getcolor(pop_up),opacity=0.7))


#joiming  the feature group to map object
map1.add_child(fgp)
map1.add_child(fg)
map1.add_child(folium.LayerControl())
map1.save("Map1.html")

import folium
# create feature group

##parent of feture group
fg=folium.FeatureGroup("My Map")

##child
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[18.5204,73.8567],popup="Taj Mahal"))

map=folium.Map(Location=[27.1751,78.0421],zoom_start=5)

map.add_child(fg)
map.save("test.html")
             


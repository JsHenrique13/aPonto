import geocoder
from geopy.geocoders import Nominatim 
import socket


"""
pclog = socket.gethostbyname(socket.gethostname())
g = geocoder.ip(pclog)
print(g.json)
"""

"""g = geocoder.ip('me')
g.latlng

lat = g.latlng[0]
lng = g.latlng[1]
print(lat, lng)"""

geolocator = Nominatim(user_agent="geoapiExercises")
place = "Itaperi rua inglaterra"
location = geolocator.geocode(place) 
print(location)
data = location.raw 
print(data)
 
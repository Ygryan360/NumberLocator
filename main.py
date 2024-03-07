import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

num = "+22897830013"
monNum = phonenumbers.parse(num)
localisation = geocoder.descriptioon_for_number(monNum, "fr")
print(localisation)

operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))

clef = "680f6bc6fa2a42bc8b2c8f21287fcea5"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
# print(reponse)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat, lng)

# Création de la carte
monMap = folium.Map(location=[lat,lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save("map.html")
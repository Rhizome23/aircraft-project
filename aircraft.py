from opensky_api import OpenSkyApi

#bboxFrance= [min_latitude, max_latitude, min_longitude, max_latitude]
bboxFrance= [37.788, 54.008, -11.514, 31.33]

# Convert longitude latitude to meter mercator
def convert(*args):
    try:
      easting, northing = transform(
        Proj(init='epsg:4326'), Proj(init='epsg:3857'), args[0], args[1])
      return easting, northing, args[2]
    except:
      return None, None



#  fly data
data =[]
api = OpenSkyApi()
states = api.get_states(bbox=bboxFrance)
for s in states.states:
    #print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.velocity, s.callsign))
    if s.latitude != None and s.longitude != None:
       data.append((float(s.longitude), float(s.latitude), s.callsign))
    else :
        pass
print(data[0:5]) 

# Données convertie au format metres mercartor
data2 =[]
for x in data:
    print(x)
    data2.append(convert(x[0],x[1],x[2]))
print("Données convertie en metres mercator")
print(data2[0:5])

# On centre la carte sur Paris
paris_lat = 48.8534
paris_long = 2.3488
coord= convert(paris_long,paris_lat, None)
print(coord)



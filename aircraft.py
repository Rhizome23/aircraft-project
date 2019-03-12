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



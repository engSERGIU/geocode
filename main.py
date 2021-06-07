from bottle import route, run, template, request
import geocoder

def get_coord(address):
    return geocoder.osm(address).latlng
def get_address(coord):
    city = geocoder.osm(coord, method='reverse').city
    country = geocoder.osm(coord, method='reverse').country
    return (city,country)


form1='''
<h1>Get coordinates</h1>
<form method='get' action='/get-coord'>
<input name='address' value='Cluj-Napoca'>
<input type='submit'>
</form>
<h1>Get address</h1>
<form method='get' action='/get-address'>
Latitude
<input name='lat' value='46.769379'>
Longitude
<input name='long' value='23.5899542'>
<input type='submit'>
</form>
'''
@route('/')
def index():
    return template(form1)

@route('/get-coord',method='GET')
def coord():
    address = request.query.address
    return str(get_coord(address))
    #return address

@route('/get-address',method='GET')
def address():
    return str(get_address([ request.query.lat, request.query.long]))


run(host='localhost', port=8080)


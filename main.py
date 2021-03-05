import urllib.request as urllib
import json
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from datetime import datetime


def get_json_object():
	req = urllib.Request("http://api.open-notify.org/iss-now.json")
	response = urllib.urlopen(req)

	obj = json.loads(response.read())

	return obj

'''Returned JSON :
{
  "message": "success", 
  "timestamp": UNIX_TIME_STAMP, 
  "iss_position": {
    "latitude": CURRENT_LATITUDE, 
    "longitude": CURRENT_LONGITUDE
  }
}
'''
def get_longitude_lattitude(json_object):

	if json_object["message"] != "success":
		raise Exception("There is a problem on getting data")


	return {"longitude":json_object['iss_position']['longitude'],
	"latitude":json_object['iss_position']['latitude']}

def plot_geographic_inf(dict_of_coord):
	ax = plt.axes(projection=ccrs.PlateCarree())
	ax.stock_img()
	ax.plot(float(dict_of_coord["longitude"]),float(dict_of_coord["latitude"]),marker=".", markersize=5,
		transform=ccrs.Geodetic(),
		color = "red")
	plt.show()


if __name__ == "__main__":


	json_object = get_json_object()
	print(datetime.fromtimestamp(json_object["timestamp"]))
	dict_of_coord = get_longitude_lattitude(json_object)
	print(float(dict_of_coord["longitude"]),float(dict_of_coord["latitude"]))
	plot_geographic_inf(dict_of_coord)




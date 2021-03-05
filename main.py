import urllib.request as urllib
import json
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def get_json_object():
	req = urllib.Request("http://api.open-notify.org/iss-now.json")
	response = urllib.urlopen(req)

	obj = json.loads(response.read())

	return obj


def get_longitude_lattitude(json_object):
	return {"longitude":json_object['iss_position']['longitude'],
	"latitude":json_object['iss_position']['latitude']}

def plot_geographic_inf(dict_of_coord):
	ax = plt.axes(projection=ccrs.PlateCarree())
	ax.stock_img()
	ax.plot(float(dict_of_coord["longitude"]),float(dict_of_coord["latitude"]),marker=".", markersize=5,transform=ccrs.Geodetic())
	plt.show()


if __name__ == "__main__":
	while(True):
		json_object = get_json_object()
		dict_of_coord = get_longitude_lattitude(json_object)
		print(float(dict_of_coord["longitude"]),float(dict_of_coord["latitude"]))
		plot_geographic_inf(dict_of_coord)




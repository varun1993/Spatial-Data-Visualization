import math

f1=open('./spiro.kml', 'w+')


R = 0.005
r = 0.001
a = 0.004
x0 = 34.021185
y0 = -118.288963
c = (x0, y0)

cos = math.cos
sin = math.sin
pi = math.pi
n = 20

t = 0.00

f1.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://earth.google.com/kml/2.0\">\n<Document>\n")
f1.write("<Style id=\"z1\"><IconStyle><Icon><href>http://www.google.com/intl/en_us/mapfiles/ms/micons/blue-dot.png</href></Icon></IconStyle></Style>\n")
f1.write("<Placemark><name>SGM</name><styleUrl>#z1</styleUrl><Point><coordinates>-118.288963,34.021185</coordinates></Point></Placemark>")
f1.write("<Placemark><name>Spirograph</name><LineString><extrude>1</extrude><tessellate>1</tessellate><coordinates>\n")
while (t < pi*n):
	x = (R + r) * cos((r / R) * t) - a * cos(((1 + (r / R)) * t))
	y = (R + r) * sin((r / R) * t) - a * sin(((1 + (r / R)) * t))
	# cx = c[0]
	# cy = c[1]
	c = (x0 + x, y0 + y)
	t += 0.01
	
	f1.write("%f,%f,0\n" % (c[1], c[0]))
	# print("x: " + str(x))
	# print("y: " + str(y))
f1.write("</coordinates></LineString><Style><LineStyle><color>#ff00ff00</color><width>5</width></LineStyle></Style></Placemark></Document></kml>")
f1.close()
print("spiro.kml file created")
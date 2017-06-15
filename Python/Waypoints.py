#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re#, datetime
#starttime = datetime.datetime.now()

#***gpx***
filepath = input("Input filepath to your gpx: ")
if filepath[-4:] != ".gpx":
	filepath = filepath + ".gpx"

gpx = open(filepath, encoding="utf8").read()
global kml
global A
global B
global x
global split

#***kml tyylipohja***
#kml = open('Waypoints.kml').read()
kml = '''<?xml version='1.0' encoding='UTF-8'?>					
<kml xmlns='http://www.opengis.net/kml/2.2'>					
	<Document>				
		<name>Waypoints</name>			
		<Style id='icon-1594-1A237E-normal'>			
			<IconStyle>		
				<color>ff7E231A</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1594-1A237E-highlight'>			
			<IconStyle>		
				<color>ff7E231A</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1594-1A237E'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1594-1A237E-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1594-1A237E-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1625-4E342E-normal'>			
			<IconStyle>		
				<color>ff2E344E</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1625-4E342E-highlight'>			
			<IconStyle>		
				<color>ff2E344E</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1625-4E342E'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1625-4E342E-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1625-4E342E-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1899-0288D1-normal'>			
			<IconStyle>		
				<color>ffD18802</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1899-0288D1-highlight'>			
			<IconStyle>		
				<color>ffD18802</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1899-0288D1'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1899-0288D1-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1899-0288D1-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1899-0F9D58-normal'>			
			<IconStyle>		
				<color>ff589D0F</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1899-0F9D58-highlight'>			
			<IconStyle>		
				<color>ff589D0F</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1899-0F9D58'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1899-0F9D58-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1899-0F9D58-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1899-757575-normal'>			
			<IconStyle>		
				<color>ff757575</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1899-757575-highlight'>			
			<IconStyle>		
				<color>ff757575</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1899-757575'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1899-757575-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1899-757575-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1899-9C27B0-normal'>			
			<IconStyle>		
				<color>ffB0279C</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1899-9C27B0-highlight'>			
			<IconStyle>		
				<color>ffB0279C</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1899-9C27B0'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1899-9C27B0-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1899-9C27B0-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1899-C2185B-normal'>			
			<IconStyle>		
				<color>ff5B18C2</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1899-C2185B-highlight'>			
			<IconStyle>		
				<color>ff5B18C2</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1899-C2185B'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1899-C2185B-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1899-C2185B-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1899-F57C00-normal'>			
			<IconStyle>		
				<color>ff007CF5</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1899-F57C00-highlight'>			
			<IconStyle>		
				<color>ff007CF5</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1899-F57C00'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1899-F57C00-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1899-F57C00-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
		<Style id='icon-1899-FFEA00-normal'>			
			<IconStyle>		
				<color>ff00EAFF</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>0.0</scale>	
			</LabelStyle>		
		</Style>			
		<Style id='icon-1899-FFEA00-highlight'>			
			<IconStyle>		
				<color>ff00EAFF</color>	
				<scale>1.0</scale>	
				<Icon>	
					<href>http://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
				</Icon>	
			</IconStyle>		
			<LabelStyle>		
				<scale>1.0</scale>	
			</LabelStyle>		
		</Style>			
		<StyleMap id='icon-1899-FFEA00'>			
			<Pair>		
				<key>normal</key>	
				<styleUrl>#icon-1899-FFEA00-normal</styleUrl>	
			</Pair>		
			<Pair>		
				<key>highlight</key>	
				<styleUrl>#icon-1899-FFEA00-highlight</styleUrl>	
			</Pair>		
		</StyleMap>			
	</Document>				
</kml>'''

#A = kml.find("<name>")+len("<name>")
#B = kml.find("</name>")
#kml = kml[:A]+"Waypoints "+starttime.strftime("%d.%m.%Y")+kml[B:]
split = kml.find("</name>\t\t\t\n")+len("</name>\t\t\t\n")

A = 0
B = 0
x = 0
def wpsearch(A, B, x, kml):
	A = gpx.find('''<wpt lat="''',B)
	if A != -1:
		B = gpx.find("</wpt>",A)+len("</wpt>")
		WP = gpx[A:B]
		x = x + 1
		#Point info:
		code = WP[WP.find("<name>")+len("<name>"):WP.find("</name>")]
		if code[0:2] == "GC":
			lat = WP[len('''<wpt lat="'''):WP.find('''"''',len('''<wpt lat="'''))]
			lon = WP[WP.find('''" lon="''')+len('''" lon="'''):WP.find('''"''',WP.find('''" lon="''')+len('''" lon="'''))]
			name = WP[WP.find("<groundspeak:name>")+len("<groundspeak:name>"):WP.find("</groundspeak:name>")] #.replace('&amp;','&')
			#info = WP[WP.find("<desc>")+len("<desc>"):WP.find("</desc>")].replace('&amp;','&')
			D = WP[WP.find("<groundspeak:difficulty>")+len("<groundspeak:difficulty>"):WP.find("</groundspeak:difficulty>")]
			T = WP[WP.find("<groundspeak:terrain>")+len("<groundspeak:terrain>"):WP.find("</groundspeak:terrain>")]
			Type = WP[WP.find("<groundspeak:type>")+len("<groundspeak:type>"):WP.find("</groundspeak:type>")]
			link = '''<a href="https://coord.info/'''+code+'''">'''+Type+"</a>"
			Container = WP[WP.find("<groundspeak:container>")+len("<groundspeak:container>"):WP.find("</groundspeak:container>")]
			DT = "("+D+"/"+T+")"
			hint = "Vihje: "+WP[WP.find("<groundspeak:encoded_hints>")+len("<groundspeak:encoded_hints>"):WP.find("</groundspeak:encoded_hints>")]
			if len(hint) == len("Vihje: "):
				hint = "Ei vihjettä"
			if Type == "Traditional Cache":
				style = "#icon-1899-0F9D58"
			elif Type == "Multi-cache":
				style = "#icon-1899-F57C00"
			elif Type == "Unknown Cache":
				style = "#icon-1594-1A237E"
			elif Type == "Letterbox Hybrid":
				style = "#icon-1899-C2185B"
			elif Type == "Wherigo Cache":
				style = "#icon-1899-9C27B0"	
			elif Type == "Earthcache":
				style = "#icon-1899-757575"		
			elif Type == "Event Cache" or Type == "Cache In Trash Out Event" or Type == "Mega-Event Cache" or Type == "Giga-Event Cache":
				style = "#icon-1625-4E342E"
			else:
				style = "#icon-1899-0288D1-nodesc"
			
			description = ""
			if WP.find('''<groundspeak:short_description html="False">''') != -1:
				description = WP[WP.find('''<groundspeak:short_description html="False">''')+len('''<groundspeak:short_description html="False">'''):WP.find('''</groundspeak:short_description>''')]
				description = description+" "+WP[WP.find('''<groundspeak:long_description html="False">''')+len('''<groundspeak:long_description html="False">'''):WP.find('''</groundspeak:long_description>''')]
			else:
				description = WP[WP.find('''<groundspeak:short_description html="True">''')+len('''<groundspeak:short_description html="True">'''):WP.find('''</groundspeak:short_description>''')]
				description = description+" "+WP[WP.find('''<groundspeak:long_description html="True">''')+len('''<groundspeak:long_description html="True">'''):WP.find('''</groundspeak:long_description>''')]
				description = description.replace("&lt;","<").replace("&gt;",">")
				while description.find("<") != -1:
					description = description[:description.find("<")]+description[description.find(">")+1:]
			Attributes = ""
			if WP.find("<groundspeak:attributes>") != -1:
				Attr = WP[WP.find("<groundspeak:attributes>")+len("<groundspeak:attributes>"):WP.find("</groundspeak:attributes>")]
				while Attr.find('''">''') != -1:
					Attr = Attr[Attr.find('''">''')+2:]
					Attributes = Attributes + " '" + Attr[0:Attr.find("<")] + "'"
				if len(Attributes) > 0:
					Attributes = "<br>Attributes:" + Attributes
				else:
					Attributes = "<br>No Attributes"
			#Add waypoint to kml
			CDATA = link+"<br>DT: "+DT+" Size: "+Container+"<br>"+hint+"<br><br>"+description+"<br>"+Attributes
			PAYLOAD = "\t\t<Placemark>\t\t\t\n\t\t<description><![CDATA["+CDATA+"]]></description>\t\t\t\n\t\t\t<name>"+name+"</name>\t\t\n\t\t\t<styleUrl>"+style+"</styleUrl>\t\t\n\t\t\t<Point>\t\t\n\t\t\t\t<coordinates>"+lon+","+lat+",0.0</coordinates>\t\n\t\t\t</Point>\t\t\n\t\t</Placemark>\t\t\t\n"
			kml = kml[:split]+PAYLOAD+kml[split:]
	else:
		print("\nFinished ("+str(x)+"kpl)")
		#print("\nFinished ("+str(x)+"kpl)",datetime.datetime.now()-starttime)
		#print(kml)
	return(A, B, x, kml)	

while A != -1:
	A, B, x, kml = wpsearch(A, B, x, kml)

tiedostonimi = "Reittipisteet.kml"	
#tiedostonimi = "Waypoints" + starttime.strftime("%d_%m_%Y") + ".kml"
with open(tiedostonimi, "w", encoding='utf-8') as f:
    f.write(kml)
print(tiedostonimi,"Done!")
input()


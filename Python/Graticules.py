#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, re

filepath = input("Input filepath to your GSAK refreshed All Finds gpx: ")
if filepath[-4:] != ".gpx":
	filepath = filepath + ".gpx"

gpx = open(filepath, encoding="utf8").read()
wpts = re.findall(r'<wpt(.*?)</wpt>',gpx,re.DOTALL)
grats = []
finds = []

for E in range(20,25):
	grats.append("N59E"+str(E))
for E in range(19,29):
	grats.append("N60E"+str(E))
for E in range(21,31):
	grats.append("N61E"+str(E))
for E in range(20,32):
	grats.append("N62E"+str(E))	
for E in range(20,32):
	grats.append("N63E"+str(E))
for E in range(23,31):
	grats.append("N64E"+str(E))
for E in range(24,31):
	grats.append("N65E"+str(E))
for E in range(23,30):
	grats.append("N66E"+str(E))
for E in range(23,30):
	grats.append("N67E"+str(E))
for E in range(20,30):
	grats.append("N68E"+str(E))
for E in range(20,23):
	grats.append("N69E"+str(E))
for E in range(25,30):
	grats.append("N69E"+str(E))
for E in range(27,29):
	grats.append("N70E"+str(E))

for kpl in range(0,len(grats)):
	finds.append(0)

for i in range(0,len(wpts)):
	GC = re.findall(r'<name>(.*?)</name>',wpts[i])[0]
	maa = re.findall(r'<groundspeak:country>(.*?)</groundspeak:country>',wpts[i])[0]
	if ((maa == 'Finland' or maa == 'Aland Islands') and (GC != 'GCGW7N' and GC != 'GCC5EE')):
		latlon = re.findall(r'(lat|lon)="(.*?)\.',wpts[i])
		grat = "N"+latlon[0][1]+"E"+latlon[1][1]
		finds[grats.index(grat)] = finds[grats.index(grat)] + 1

kml = '''<?xml version='1.0' encoding='UTF-8'?>						
<kml xmlns='http://www.opengis.net/kml/2.2'>						
	<Document>					
		<name>Graticulet</name>				
		<Placemark>				
			<name>N59E20</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>20,59,0.0 21,59,0.0 21,60,0.0 20,60,0.0 20,59,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N59E21</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>21,59,0.0 22,59,0.0 22,60,0.0 21,60,0.0 21,59,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N59E22</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>22,59,0.0 23,59,0.0 23,60,0.0 22,60,0.0 22,59,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N59E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,59,0.0 24,59,0.0 24,60,0.0 23,60,0.0 23,59,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N59E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,59,0.0 25,59,0.0 25,60,0.0 24,60,0.0 24,59,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E19</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>19,60,0.0 20,60,0.0 20,61,0.0 19,61,0.0 19,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E20</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>20,60,0.0 21,60,0.0 21,61,0.0 20,61,0.0 20,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E21</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>21,60,0.0 22,60,0.0 22,61,0.0 21,61,0.0 21,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E22</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>22,60,0.0 23,60,0.0 23,61,0.0 22,61,0.0 22,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,60,0.0 24,60,0.0 24,61,0.0 23,61,0.0 23,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,60,0.0 25,60,0.0 25,61,0.0 24,61,0.0 24,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,60,0.0 26,60,0.0 26,61,0.0 25,61,0.0 25,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,60,0.0 27,60,0.0 27,61,0.0 26,61,0.0 26,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,60,0.0 28,60,0.0 28,61,0.0 27,61,0.0 27,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N60E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,60,0.0 29,60,0.0 29,61,0.0 28,61,0.0 28,60,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E21</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>21,61,0.0 22,61,0.0 22,62,0.0 21,62,0.0 21,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E22</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>22,61,0.0 23,61,0.0 23,62,0.0 22,62,0.0 22,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,61,0.0 24,61,0.0 24,62,0.0 23,62,0.0 23,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,61,0.0 25,61,0.0 25,62,0.0 24,62,0.0 24,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,61,0.0 26,61,0.0 26,62,0.0 25,62,0.0 25,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,61,0.0 27,61,0.0 27,62,0.0 26,62,0.0 26,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,61,0.0 28,61,0.0 28,62,0.0 27,62,0.0 27,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,61,0.0 29,61,0.0 29,62,0.0 28,62,0.0 28,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,61,0.0 30,61,0.0 30,62,0.0 29,62,0.0 29,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N61E30</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>30,61,0.0 31,61,0.0 31,62,0.0 30,62,0.0 30,61,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E20</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>20,62,0.0 21,62,0.0 21,63,0.0 20,63,0.0 20,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E21</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>21,62,0.0 22,62,0.0 22,63,0.0 21,63,0.0 21,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E22</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>22,62,0.0 23,62,0.0 23,63,0.0 22,63,0.0 22,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,62,0.0 24,62,0.0 24,63,0.0 23,63,0.0 23,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,62,0.0 25,62,0.0 25,63,0.0 24,63,0.0 24,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,62,0.0 26,62,0.0 26,63,0.0 25,63,0.0 25,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,62,0.0 27,62,0.0 27,63,0.0 26,63,0.0 26,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,62,0.0 28,62,0.0 28,63,0.0 27,63,0.0 27,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,62,0.0 29,62,0.0 29,63,0.0 28,63,0.0 28,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,62,0.0 30,62,0.0 30,63,0.0 29,63,0.0 29,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E30</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>30,62,0.0 31,62,0.0 31,63,0.0 30,63,0.0 30,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N62E31</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>31,62,0.0 32,62,0.0 32,63,0.0 31,63,0.0 31,62,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E20</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>20,63,0.0 21,63,0.0 21,64,0.0 20,64,0.0 20,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E21</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>21,63,0.0 22,63,0.0 22,64,0.0 21,64,0.0 21,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E22</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>22,63,0.0 23,63,0.0 23,64,0.0 22,64,0.0 22,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,63,0.0 24,63,0.0 24,64,0.0 23,64,0.0 23,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,63,0.0 25,63,0.0 25,64,0.0 24,64,0.0 24,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,63,0.0 26,63,0.0 26,64,0.0 25,64,0.0 25,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,63,0.0 27,63,0.0 27,64,0.0 26,64,0.0 26,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,63,0.0 28,63,0.0 28,64,0.0 27,64,0.0 27,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,63,0.0 29,63,0.0 29,64,0.0 28,64,0.0 28,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,63,0.0 30,63,0.0 30,64,0.0 29,64,0.0 29,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E30</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>30,63,0.0 31,63,0.0 31,64,0.0 30,64,0.0 30,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N63E31</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>31,63,0.0 32,63,0.0 32,64,0.0 31,64,0.0 31,63,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,64,0.0 24,64,0.0 24,65,0.0 23,65,0.0 23,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,64,0.0 25,64,0.0 25,65,0.0 24,65,0.0 24,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,64,0.0 26,64,0.0 26,65,0.0 25,65,0.0 25,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,64,0.0 27,64,0.0 27,65,0.0 26,65,0.0 26,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,64,0.0 28,64,0.0 28,65,0.0 27,65,0.0 27,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,64,0.0 29,64,0.0 29,65,0.0 28,65,0.0 28,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,64,0.0 30,64,0.0 30,65,0.0 29,65,0.0 29,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N64E30</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>30,64,0.0 31,64,0.0 31,65,0.0 30,65,0.0 30,64,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N65E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,65,0.0 25,65,0.0 25,66,0.0 24,66,0.0 24,65,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N65E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,65,0.0 26,65,0.0 26,66,0.0 25,66,0.0 25,65,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N65E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,65,0.0 27,65,0.0 27,66,0.0 26,66,0.0 26,65,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N65E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,65,0.0 28,65,0.0 28,66,0.0 27,66,0.0 27,65,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N65E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,65,0.0 29,65,0.0 29,66,0.0 28,66,0.0 28,65,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N65E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,65,0.0 30,65,0.0 30,66,0.0 29,66,0.0 29,65,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N65E30</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>30,65,0.0 31,65,0.0 31,66,0.0 30,66,0.0 30,65,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N66E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,66,0.0 24,66,0.0 24,67,0.0 23,67,0.0 23,66,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N66E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,66,0.0 25,66,0.0 25,67,0.0 24,67,0.0 24,66,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N66E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,66,0.0 26,66,0.0 26,67,0.0 25,67,0.0 25,66,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N66E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,66,0.0 27,66,0.0 27,67,0.0 26,67,0.0 26,66,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N66E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,66,0.0 28,66,0.0 28,67,0.0 27,67,0.0 27,66,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N66E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,66,0.0 29,66,0.0 29,67,0.0 28,67,0.0 28,66,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N66E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,66,0.0 30,66,0.0 30,67,0.0 29,67,0.0 29,66,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N67E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,67,0.0 24,67,0.0 24,68,0.0 23,68,0.0 23,67,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N67E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,67,0.0 25,67,0.0 25,68,0.0 24,68,0.0 24,67,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N67E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,67,0.0 26,67,0.0 26,68,0.0 25,68,0.0 25,67,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N67E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,67,0.0 27,67,0.0 27,68,0.0 26,68,0.0 26,67,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N67E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,67,0.0 28,67,0.0 28,68,0.0 27,68,0.0 27,67,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N67E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,67,0.0 29,67,0.0 29,68,0.0 28,68,0.0 28,67,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N67E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,67,0.0 30,67,0.0 30,68,0.0 29,68,0.0 29,67,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E20</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>20,68,0.0 21,68,0.0 21,69,0.0 20,69,0.0 20,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E21</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>21,68,0.0 22,68,0.0 22,69,0.0 21,69,0.0 21,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E22</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>22,68,0.0 23,68,0.0 23,69,0.0 22,69,0.0 22,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E23</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>23,68,0.0 24,68,0.0 24,69,0.0 23,69,0.0 23,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E24</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>24,68,0.0 25,68,0.0 25,69,0.0 24,69,0.0 24,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,68,0.0 26,68,0.0 26,69,0.0 25,69,0.0 25,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,68,0.0 27,68,0.0 27,69,0.0 26,69,0.0 26,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,68,0.0 28,68,0.0 28,69,0.0 27,69,0.0 27,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,68,0.0 29,68,0.0 29,69,0.0 28,69,0.0 28,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N68E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,68,0.0 30,68,0.0 30,69,0.0 29,69,0.0 29,68,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E20</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>20,69,0.0 21,69,0.0 21,70,0.0 20,70,0.0 20,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E21</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>21,69,0.0 22,69,0.0 22,70,0.0 21,70,0.0 21,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E22</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>22,69,0.0 23,69,0.0 23,70,0.0 22,70,0.0 22,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E25</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>25,69,0.0 26,69,0.0 26,70,0.0 25,70,0.0 25,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E26</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>26,69,0.0 27,69,0.0 27,70,0.0 26,70,0.0 26,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,69,0.0 28,69,0.0 28,70,0.0 27,70,0.0 27,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,69,0.0 29,69,0.0 29,70,0.0 28,70,0.0 28,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N69E29</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>29,69,0.0 30,69,0.0 30,70,0.0 29,70,0.0 29,69,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N70E27</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>27,70,0.0 28,70,0.0 28,71,0.0 27,71,0.0 27,70,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>				
		<Placemark>				
			<name>N70E28</name>			
			<description><![CDATA[0]]></description>			
			<styleUrl>#poly-DB4436-1-64</styleUrl>			
			<Polygon>			
				<outerBoundaryIs>		
					<LinearRing>	
						<tessellate>1</tessellate>
						<coordinates>28,70,0.0 29,70,0.0 29,71,0.0 28,71,0.0 28,70,0.0</coordinates>
					</LinearRing>	
				</outerBoundaryIs>		
			</Polygon>			
		</Placemark>		
		<Style id='poly-00D079-1-59-normal'>				
			<LineStyle>			
				<color>ff79D000</color>		
				<width>1</width>		
			</LineStyle>			
			<PolyStyle>			
				<color>3B79D000</color>		
				<fill>1</fill>		
				<outline>1</outline>		
			</PolyStyle>			
		</Style>				
		<Style id='poly-00D079-1-59-highlight'>				
			<LineStyle>			
				<color>ff79D000</color>		
				<width>2.0</width>		
			</LineStyle>			
			<PolyStyle>			
				<color>3B79D000</color>		
				<fill>1</fill>		
				<outline>1</outline>		
			</PolyStyle>			
		</Style>				
		<StyleMap id='poly-00D079-1-59'>				
			<Pair>			
				<key>normal</key>		
				<styleUrl>#poly-00D079-1-59-normal</styleUrl>		
			</Pair>			
			<Pair>			
				<key>highlight</key>		
				<styleUrl>#poly-00D079-1-59-highlight</styleUrl>		
			</Pair>			
		</StyleMap>				
		<Style id='poly-DB4436-1-64-normal'>				
			<LineStyle>			
				<color>ff3644DB</color>		
				<width>1</width>		
			</LineStyle>			
			<PolyStyle>			
				<color>403644DB</color>		
				<fill>1</fill>		
				<outline>1</outline>		
			</PolyStyle>			
		</Style>				
		<Style id='poly-DB4436-1-64-highlight'>				
			<LineStyle>			
				<color>ff3644DB</color>		
				<width>2.0</width>		
			</LineStyle>			
			<PolyStyle>			
				<color>403644DB</color>		
				<fill>1</fill>		
				<outline>1</outline>		
			</PolyStyle>			
		</Style>				
		<StyleMap id='poly-DB4436-1-64'>				
			<Pair>			
				<key>normal</key>		
				<styleUrl>#poly-DB4436-1-64-normal</styleUrl>		
			</Pair>			
			<Pair>			
				<key>highlight</key>		
				<styleUrl>#poly-DB4436-1-64-highlight</styleUrl>		
			</Pair>			
		</StyleMap>				
	</Document>					
</kml>						
'''

found = 0
for i in range(0,len(grats)):
	A = re.search('<name>'+grats[i]+'</name>',kml).end()
	if finds[i] > 0:
		A = kml.find('<description><![CDATA[',A)+len('<description><![CDATA[')
		B = kml.find(']]></description>',A)
		kml = kml[:A]+str(finds[i])+kml[B:]
		A = kml.find('<styleUrl>',A)+len('<styleUrl>')
		B = kml.find('</styleUrl>',A)
		kml = kml[:A]+'#poly-00D079-1-59'+kml[B:]
		found = found + 1

with open("Graticulet.kml", "w") as f:
    f.write(kml)
#print(kml)
print('Graticulet.kml DONE\nFound '+str(found)+"/"+str(len(grats)))
input()
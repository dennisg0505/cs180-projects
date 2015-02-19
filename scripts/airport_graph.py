

#------------------------------------------------------------------------------------------
#   US airport graph generator
#
#   Given an input .csv file (on standard input)
#   this generates a .svg file with the airport graph
#
#   From a terminal command line, use a command like:
#
#        python airport_graph.py  <  my_edges.csv  >  my_graph.svg
#
#   The input file of edges can just be pairs of airports, like:
#
#   LAX,ABQ
#   ABQ,DEN
#   DEN,DFW
#   ...
#
#------------------------------------------------------------------------------------------


import sys
import csv

#------------------------------------------------------------------------------------------
#   US airport data
#------------------------------------------------------------------------------------------

US_airports = """
ABQ,Albuquerque International Sunport Airport,35.0401992797852,-106.609001159668
AMA,Rick Husband Amarillo International Airport,35.2193984985352,-101.706001281738
ANC,Ted Stevens Anchorage International Airport,61.1744003295898,-149.996002197266
ATL,Hartsfield Jackson Atlanta International Airport,33.6366996765137,-84.4281005859375
AUS,Austin Bergstrom International Airport,30.1944999694824,-97.6698989868164
BDL,Bradley International Airport,41.9388999939,-72.6831970215
BFI,Boeing Field King County International Airport,47.5299987792969,-122.302001953125
BGR,Bangor International Airport,44.8073997497559,-68.8281021118164
BHM,Birmingham-Shuttlesworth International Airport,33.56290054,-86.75350189
BIL,Billings Logan International Airport,45.8077011108398,-108.542999267578
BNA,Nashville International Airport,36.1245002746582,-86.6781997680664
BOS,General Edward Lawrence Logan International Airport,42.36429977,-71.00520325
BUF,Buffalo Niagara International Airport,42.94049835,-78.73220062
BWI,Baltimore/Washington International Thurgood Marshal Airport,39.17539978,-76.66829681
CHS,Charleston Air Force Base-International Airport,32.89860153,-80.04049683
CLE,Cleveland Hopkins International Airport,41.4117012024,-81.8498001099
CLT,Charlotte Douglas International Airport,35.2140007019043,-80.9430999755859
CMH,Port Columbus International Airport,39.9980010986328,-82.8918991088867
CPR,Casper-Natrona County International Airport,42.90800095,-106.4639969
CRP,Corpus Christi International Airport,27.7703990936279,-97.5011978149414
CVG,Cincinnati Northern Kentucky International Airport,39.0488014221,-84.6678009033
DAY,James M Cox Dayton International Airport,39.902400970459,-84.2193984985352
DEN,Denver International Airport,39.8616981506348,-104.672996520996
DFW,Dallas Fort Worth International Airport,32.896800994873,-97.0380020141602
DLH,Duluth International Airport,46.842098236084,-92.193603515625
DSM,Des Moines International Airport,41.5340003967285,-93.6631011962891
ERI,Erie International Tom Ridge Field,42.0820007324,-80.1762008667
EWR,Newark Liberty International Airport,40.6925010681152,-74.168701171875
FAI,Fairbanks International Airport,64.81510162,-147.8560028
FLL,Fort Lauderdale Hollywood International Airport,26.0725994110107,-80.152702331543
FWA,Fort Wayne International Airport,40.97850037,-85.19509888
GEG,Spokane International Airport,47.6198997497559,-117.533996582031
GPT,Gulfport Biloxi International Airport,30.4073009490967,-89.0700988769531
GRB,Austin Straubel International Airport,44.4850997924805,-88.1296005249023
GSO,Piedmont Triad International Airport,36.0978012084961,-79.9373016357422
GSP,Greenville Spartanburg International Airport,34.8956985474,-82.2189025879
HNL,Honolulu International Airport,21.3187007904053,-157.921997070312
HSV,Huntsville International Carl T Jones Field,34.6371994018555,-86.7751007080078
IAD,Washington Dulles International Airport,38.94449997,-77.45580292
IAH,George Bush Intercontinental Houston Airport,29.9843997955322,-95.3414001464844
ICT,Wichita Mid Continent Airport,37.6498985290527,-97.4330978393555
IND,Indianapolis International Airport,39.7173004150391,-86.2944030761719
JAN,Jackson Evers International Airport,32.3111991882324,-90.0758972167969
JAX,Jacksonville International Airport,30.4941005706787,-81.6878967285156
JFK,John F Kennedy International Airport,40.63980103,-73.77890015
LAS,McCarran International Airport,36.08010101,-115.1520004
LAX,Los Angeles International Airport,33.94250107,-118.4079971
LBB,Lubbock Preston Smith International Airport,33.6636009216309,-101.822998046875
MBS,MBS International Airport,43.532901763916,-84.0795974731445
MCI,Kansas City International Airport,39.2975997924805,-94.7138977050781
MCO,Orlando International Airport,28.4293994903564,-81.3089981079102
MDW,Chicago Midway International Airport,41.7859992980957,-87.7524032592773
MEM,Memphis International Airport,35.0424003601074,-89.9766998291016
MIA,Miami International Airport,25.7931995391846,-80.2906036376953
MKE,General Mitchell International Airport,42.9472007751465,-87.896598815918
MLI,Quad City International Airport,41.4485015869141,-90.5074996948242
MSP,Minneapolis-St Paul International/Wold-Chamberlain Airport,44.8819999695,-93.2218017578
MSY,Louis Armstrong New Orleans International Airport,29.9934005737305,-90.2580032348633
MYR,Myrtle Beach International Airport,33.6796989440918,-78.9282989501953
OAK,Metropolitan Oakland International Airport,37.7212982177734,-122.221000671387
ONT,Ontario International Airport,34.0559997558594,-117.600997924805
ORD,Chicago O'Hare International Airport,41.97859955,-87.90480042
ORF,Norfolk International Airport,36.8945999145508,-76.2012023925781
PBI,Palm Beach International Airport,26.6832008361816,-80.0955963134766
PDX,Portland International Airport,45.58869934,-122.5979996
PHF,Newport News Williamsburg International Airport,37.13190079,-76.49299622
PHL,Philadelphia International Airport,39.871898651123,-75.241096496582
PHX,Phoenix Sky Harbor International Airport,33.4342994689941,-112.012001037598
PIT,Pittsburgh International Airport,40.49150085,-80.23290253
PWM,Portland International Jetport Airport,43.64619827,-70.30930328
RDU,Raleigh Durham International Airport,35.8776016235352,-78.7874984741211
RFD,Chicago Rockford International Airport,42.1954002380371,-89.0971984863281
RIC,Richmond International Airport,37.505199432373,-77.3197021484375
RNO,Reno Tahoe International Airport,39.4990997314453,-119.767997741699
ROC,Greater Rochester International Airport,43.1189002990723,-77.6724014282227
RST,Rochester International Airport,43.9082984924316,-92.5
RSW,Southwest Florida International Airport,26.5361995697021,-81.7552032470703
SAN,San Diego International Airport,32.7336006164551,-117.190002441406
SAT,San Antonio International Airport,29.5337009429932,-98.4698028564453
SAV,Savannah Hilton Head International Airport,32.12760162,-81.20210266
SDF,Louisville International Standiford Field,38.1744003295898,-85.7360000610352
SEA,Seattle Tacoma International Airport,47.4490013122559,-122.30899810791
SFB,Orlando Sanford International Airport,28.7775993347168,-81.2375030517578
SFO,San Francisco International Airport,37.6189994812012,-122.375
SJC,Norman Y. Mineta San Jose International Airport,37.3625984191895,-121.929000854492
SLC,Salt Lake City International Airport,40.7883987426758,-111.977996826172
SMF,Sacramento International Airport,38.6954002380371,-121.591003417969
SRQ,Sarasota Bradenton International Airport,27.3953990936279,-82.5543975830078
STL,Lambert St Louis International Airport,38.7486991882324,-90.370002746582
SYR,Syracuse Hancock International Airport,43.111198425293,-76.1063003540039
TPA,Tampa International Airport,27.9755001068115,-82.533203125
TUL,Tulsa International Airport,36.1983985900879,-95.8880996704102
TUS,Tucson International Airport,32.1161003112793,-110.94100189209
"""

US_airport_table = [line.strip().split(",") for line in US_airports.split("\n") if line.strip() != '']

US_airports = [row[0] for row in US_airport_table]

US_airport_lat_lon = dict([(row[0], (float(row[2]),float(row[3]))) for row in US_airport_table if len(row)>=3])

#------------------------------------------------------------------------------------------
#   Read in edges (pairs of airport 3-letter codes) from standard input
#------------------------------------------------------------------------------------------

input_edges = set([])

with sys.stdin as input:
    reader = csv.reader(input)
    edge_table = [row for row in reader]
    starting_row = 0
    if len(edge_table[0])>2:
        if len(edge_table[0][1]) != 3:    # skip the first (header) row if there is one
            starting_row = 1
    for edge in edge_table[starting_row:]:
        origin = edge[0].strip()
        dest   = edge[1].strip()
        input_edges.add((origin,dest))

#------------------------------------------------------------------------------------------
#   Lat/Lon manipulation
#------------------------------------------------------------------------------------------

def ceil(x):
   return int(x+1)

def floor(x):
   return int(x)

max_lat = ceil ( max( [US_airport_lat_lon[airport][0] for airport in US_airports] ) )
min_lat = floor( min( [US_airport_lat_lon[airport][0] for airport in US_airports] ) )
max_lon = ceil ( max( [US_airport_lat_lon[airport][1] for airport in US_airports] ) )
min_lon = floor( min( [US_airport_lat_lon[airport][1] for airport in US_airports] ) )



x_size = 800 # px 
y_size = 600 # px 

x_scale = x_size / (max_lon - min_lon + 2)
y_scale = y_size / (max_lat - min_lat + 2)

def yvalue(y):
   return ((max_lat - y + 2) * y_scale)

def xvalue(x):
   return ((x - min_lon + 2) * x_scale)

max_yvalue = yvalue(max_lat + 2)
min_yvalue = yvalue(min_lat - 2)
max_xvalue = xvalue(max_lon + 2)
min_xvalue = xvalue(min_lon - 2)

#------------------------------------------------------------------------------------------
#   SVG templates
#------------------------------------------------------------------------------------------


svg_header = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg 
         width="{width}"
         height="{height}"
         viewBox="0 0 {width} {height}"
     xmlns="http://www.w3.org/2000/svg" version="1.1">
<desc>US Airports Graph</desc>
<title>US Airports</title>
<g font-size="18" font-family="Verdana"><text x="{xhead}" y="{yhead}">US Airports</text></g>
""".format( x1 = min_xvalue, x2 = max_xvalue, y1 = min_yvalue, y2 = max_yvalue, width = x_size, height = y_size, xhead = x_size/2, yhead = y_size/5 )

svg_trailer = """
</svg>
"""

def svg_node_template(airport_name):
   lat, lon = US_airport_lat_lon[airport_name]
   return """<text x="%.2f" y="%.2f">%s</text>""" % (xvalue(lon), yvalue(lat), airport_name)

def svg_edge_template(origin,dest):
   origin_lat, origin_lon = US_airport_lat_lon[origin]
   dest_lat,   dest_lon   = US_airport_lat_lon[dest]
   return """<!-- %s - %s --> <line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" />""" % ( origin, dest, xvalue(origin_lon), yvalue(origin_lat), xvalue(dest_lon), yvalue(dest_lat) )



#------------------------------------------------------------------------------------------
#   Generate and print the SVG
#------------------------------------------------------------------------------------------

svg_airport_nodes  = """<g font-size="7" font-family="Verdana">\n   """
svg_airport_nodes += "\n   ".join([ svg_node_template(airport) for airport in US_airports ])
svg_airport_nodes += """\n</g>\n"""

svg_airport_edges  = """<g stroke="red" stroke-width="0.1">\n   """
svg_airport_edges += "\n   ".join( [ svg_edge_template(origin,dest) for (origin,dest) in input_edges ])
svg_airport_edges += """\n</g>\n"""

svg = svg_header + svg_airport_edges + svg_airport_nodes + svg_trailer

print(svg)

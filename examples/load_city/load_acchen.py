from sumo_pts.map.city import City


aachen = City('osm.net.xml')

aachen.change_street_speed('Pontwall', 0.1)
aachen.save('osm_slow.net.xml')

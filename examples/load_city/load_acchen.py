from sumo_pts.map.city import City


aachen = City('osm.net.xml', 'osm_pt.rou.xml')

aachen.change_street_speed('Pontwall', 0.1)
aachen.save('osm_slow.net.xml')

street_names = ['Pontwall', 'Seffenter Weg', 'Forckenbeckstraße', 'Halifaxstraße',
               'Alexianergraben', 'Franzstraße', 'Jakobstraße', 'Vaalser Straße',
               'Komphausbadstraße', 'Peterstraße', 'Heinrichsallee', 'Theaterstraße',
               'Saarstraße', 'Boxgraben', 'Roermonder Straße', 'Hirschgraben']

aachen.show_statistics()

import xml.etree.ElementTree as ET


class City:
    """
    Model roads and bus transportaion system of a city.

    Attributes
    ----------
    net_file_path: str
        path to xml network file

    route_file_path: str
        path to xml route file

    Methods
    -------
    load_xml(self, path):
        returns the thermal diffusivity of the material

    """
    
    def __init__(self, net_file_path, route_file_path):
        self.net_file_path = net_file_path
        self.route_file_path = route_file_path
        self._load_xml()

    def _load_xml(self):
        self.net_tree = ET.parse(self.net_file_path)
        self.net_root = self.net_tree.getroot()
        self.route_tree = ET.parse(self.route_file_path)
        self.route_root = self.route_tree.getroot()

    def get_net_root(self):
        return self.net_root

    def get_route_root(self):
        return self.route_root

    def change_street_speed(self, street_name, speed_scale):
        for child1 in self.net_root:
            if child1.tag == 'edge':
                if 'name' in child1.attrib.keys(): 
                    if child1.attrib['name'] == street_name:
                        for child2 in child1:
                            if 'speed' in child2.attrib.keys():
                                # print(child2.attrib['speed'])
                                current_speed = float(child2.attrib['speed'])
                                child2.attrib['speed'] = str(speed_scale * current_speed)
                                # print(child2.attrib['speed'])
    
    def save(self, fname):
        self.net_tree.write(fname)

    def show_statistics(self, street_names=None):
        """
        Printing information about the bus trips through city streets. 

        Parameters
        ----------
        street_names = None : list of str
            a list containing the name of the streets to report the trips.
        
        Returns
        -------
        counter_edge_bus_sorted: dict
            a dictionay mapping street names (str) to number of bus trips (int).
        """
        edge_id_name = {}
        for child1 in self.net_root:
            if child1.tag == 'edge':
                if 'name' in child1.attrib.keys():
                    # if child1.attrib['name'] == edge_id_name:
                    edge_id_name[child1.attrib['id']] = child1.attrib['name']

        # return edge_id_name
        counter_edge_bus = {}
        for child1 in self.route_root:
            if child1.tag == 'route':
                if 'edges' in child1.attrib.keys():
                    for edge_id in child1.attrib['edges'].split():
                        if edge_id in edge_id_name.keys():
                            street_name = edge_id_name[edge_id]
                            if street_name in counter_edge_bus.keys():
                                counter_edge_bus[street_name] += 1
                            else:
                                counter_edge_bus[street_name] = 1
        
        counter_edge_bus_sorted = {k: v for k, v in sorted(counter_edge_bus.items(), key=lambda item: -item[1])}
        total_trips = 0
        
        print('street name \t\t # bus trips')
        print('----------- \t\t   ------------')
        for street_name in counter_edge_bus_sorted:
            if street_names != None:
                if street_name in street_names:
                    print(f'{street_name} \t\t\t {counter_edge_bus_sorted[street_name]}')
            else:
                print(f'{street_name} \t\t\t {counter_edge_bus_sorted[street_name]}')
            
            total_trips += counter_edge_bus_sorted[street_name]
        print(f'total # trips: \t\t\t {total_trips}')
        
        return counter_edge_bus_sorted

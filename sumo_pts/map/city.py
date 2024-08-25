import xml.etree.ElementTree as ET

# tree = ET.parse('tripinfo.out')
# root = tree.getroot()

# for c in root:
#     if float(c.attrib['departDelay']) > 50: 
#         print(c.attrib['id'], c.attrib['departDelay'])

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
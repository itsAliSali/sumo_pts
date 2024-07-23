import xml.etree.ElementTree as ET


class TripInfo:
    """
    Read trip information output of SUMO simualtion.

    Attributes
    ----------
    file_path: str
        path to ouput file
    delay_threshold: float or int = 0
        time threshold (seconds) to consider delay

    Methods
    -------
    get_root(self):
        returns root node of xml file
    get_total_delay(self):
        returns sum of all delays above a given threshold

    """

    def __init__(self, file_path, delay_threshold=0):
        self.file_path = file_path
        self.delay_threshold = delay_threshold
        self._load_xml()

    def _load_xml(self):
        tree = ET.parse(self.file_path)
        self.root = tree.getroot()

    def get_root(self):
        return self.root

    def get_total_delay(self):
        self.total_delay = 0 
        self.count_delays = 0 
        for child in self.root:
            delay = float(child.attrib['departDelay'])
            if delay > self.delay_threshold:
                self.total_delay += delay
                self.count_delays += 1
                # print(child.attrib['id'], child.attrib['departDelay'])
        # print(self.total_delay, self.count_delays)
        return self.total_delay
    
    def get_num_delay(self):
        return self.count_delays

# tree = ET.parse('tripinfo.out')
# root = tree.getroot()

# for c in root:
#     if float(c.attrib['departDelay']) > 50: 
#         print(c.attrib['id'], c.attrib['departDelay'])
import os
import xml.etree.ElementTree as ET


class SimConfig:
    """
    This class will prepare a configuration file for SUMO simulations.

    Attributes
    ----------
    config_path: str
        path to xml configuration file

    Methods
    -------
    change_netfile(self, netfile_name):
        Changes the network file name in configuration file

    save(self, fname):
        Writes the xml datastructure into a file on the disk 

    """

    def __init__(self, config_path):
        self.config_path = config_path
        self._load_xml()

    def _load_xml(self):
        self.tree = ET.parse(self.config_path)
        self.root = self.tree.getroot()

    def change_netfile(self, netfile_name):
        self.root[0][0].attrib['value'] = netfile_name 
    
    def save(self, fname):
        self.tree.write(fname)



class SimulationHandler:
    """
    Run a SUMO simulation to visualize the city taffic flow and generate raw outputs.

    Attributes
    ----------


    Methods
    -------
    run(self, gui):
        opens a process to run simualtion

    """

    def __init__(self, config_path):
        self.config_path = config_path

    def run(self, output_tripinfo='tripinfo.out', gui=False):
        if gui == False:
            os.popen(f"sumo -c {self.config_path} --tripinfo-output {output_tripinfo}").read()
        else:
            os.popen(f"sumo-gui -c {self.config_path}").read()
        print("Simulation finished.")

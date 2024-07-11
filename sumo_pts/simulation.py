import os


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

    def run(self, gui=False):
        if gui == False:
            os.popen(f"sumo -c {self.config_path} --statistic-output test1.sta.out --netstate-dump test1.netstate.dump.out").read()
        else:
            os.popen(f"sumo-gui -c {self.config_path}").read()
        print("Simulation finished.")

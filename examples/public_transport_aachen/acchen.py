from sumo_pts.simulation import SimulationHandler, SimConfig


# conf = SimConfig('aachen.sumocfg')
# conf.change_netfile('osm.net.xml.gz')
# conf.save('aachen.sumocfg.deleteme')

acchen_sim = SimulationHandler("aachen.sumocfg")
acchen_sim.run(gui=True)

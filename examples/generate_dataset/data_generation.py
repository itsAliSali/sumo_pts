from sumo_pts.map.city import City
from sumo_pts.simulation import SimulationHandler, SimConfig
from sumo_pts.output.tripinfo_reader import TripInfo

from scipy.stats import qmc
import numpy as np



stree_names = ['Pontwall', 'Seffenter Weg', 'Forckenbeckstraße', 'Halifaxstraße',
               'Alexianergraben', 'Franzstraße', 'Jakobstraße', 'Vaalser Straße',
               'Komphausbadstraße', 'Peterstraße', 'Heinrichsallee', 'Theaterstraße',
               'Saarstraße', 'Boxgraben', 'Roermonder Straße', 'Hirschgraben']

sampler = qmc.LatinHypercube(d=len(stree_names))
sample = sampler.random(n=10)


for i in range(sample.shape[0]):
    aachen = City('osm.net.xml', 'osm_pt.rou.xml')
    for j, street in enumerate(stree_names):
        aachen.change_street_speed(street, sample[i, j])
    aachen.save(f'./data/osm_slow_{i}.net.xml')


for i in range(sample.shape[0]):
    conf = SimConfig('aachen.sumocfg')
    conf.change_netfile(f'./data/osm_slow_{i}.net.xml')
    conf.save('aachen_1.sumocfg')

    acchen_sim = SimulationHandler("aachen_1.sumocfg")
    acchen_sim.run(output_tripinfo=f'./output/tripinfo_{i}.out', gui=False)


total_delays = []
for i in range(sample.shape[0]):
    tripinfo_output = TripInfo(f'./output/tripinfo_{i}.out', 0)
    total_delay = tripinfo_output.get_total_delay()
    num_delays = tripinfo_output.get_num_delay()
    print(f'{num_delays} delays happend. in total {total_delay:.2f} seconds. average {total_delay/num_delays:.2f} seconds')
    total_delays.append(total_delay)


total_delays = np.array(total_delays)

np.save('input.npy', sample)
np.save('output.npy', total_delays)

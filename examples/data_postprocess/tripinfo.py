from sumo_pts.output.tripinfo_reader import TripInfo


tripinfo_output = TripInfo('tripinfo.out', 50)
total_delay = tripinfo_output.get_total_delay()
num_delays = tripinfo_output.get_num_delay()

print(f'{num_delays} delays happend. in total {total_delay:.2f} seconds. average {total_delay/num_delays:.2f} seconds')

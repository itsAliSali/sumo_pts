# sumo_pts
A Python interface for simulating public transport systems using SUMO.
<br>
![](examples/public_transport_aachen/demo_aac.gif)

### Build instructions
The following instructions are tested on a Ubuntu 22.04.4 installation with Python 3.10.12 and SUMO 1.20.0.
```
python3 -m pip install .
```

### TODO
- [ ] Abstracting city map: net.xml & stops.add.xml.
- [ ] Abstract bus trips.
- [ ] Abstract car trips.
- [ ] Example: generate different transpot scenarios + making a dataset.
- [ ] Training models on the dataset.
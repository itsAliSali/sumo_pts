# sumo_pts
A Python interface for simulating public transport systems using SUMO.<br>
<br>
![](examples/public_transport_aachen/demo_aac.gif)
<br>
<br>

Urban transportation systems are becoming increasingly complex due to the growing number of vehicles and varying traffic conditions. To address these challenges, this project utilized SUMO to model the bus transportation system and road network of Aachen. The developed library can be applied to study any city. By modifying road speed limits and simulating diverse traffic scenarios, the project aimed to assess the impact of individual streets on bus delays and creating a machine learning model to predict these delays.


### Requirements
To use this library, you need to have SUMO installed on your device. Follow the instructions on the SUMO webpage specific to your operating system. Below is a quick installation guide for Linux:

```bash
sudo add-apt-repository ppa:sumo/stable
sudo apt-get update
sudo apt-get install sumo sumo-tools sumo-doc
```


### Installation instructions
To install the package available on PyPI, you can run the following command:
```bash
pip install sumo-pts
```

If you'd like to experiment with the library or develop new features, feel free to install it directly from this repository by running:
```bash
python3 -m pip install .
```


### Usage
You can now import various modules and begin using the package. Below is an example code for running a graphical simulation:

```python
from sumo_pts.simulation import SimulationHandler, SimConfig

acchen_sim = SimulationHandler("aachen.sumocfg")
acchen_sim.run(gui=True)
```


### Contributing
Contributions are highly encouraged! If you're interested in contributing, please follow the steps outlined below, and make sure that your code complies with the project's coding standards.

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a Pull Request.


### Acknowledgments
This project was developed as part of the Sustainable Computational Engineering course at RWTH-Aachen University. I would like to express my gratitude to the course instructors for their guidance throughout the project. Special thanks to the developers of SUMO and the contributors to the open-source community who made this project possible.
# Snowball Earth Theory

## Description

This is a project made in 24h during the McGill's Physics Hackathon 2020. 

This application is a simulation of a simple climate model. It computes the average temperature in relation to the latitude with some graphs for visualization.

## Dependencies

We developed it using [python 3.8.0](https://www.python.org/downloads/release/python-380/).

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these packages.

```bash
pip install pyqt5
pip install pyqt5-tools
pip install numpy
pip install matplotlib
```

## Installation

1. Clone this repository on your disk
```bash
git clone https://github.com/AggroBane/SnowballEarthTheorem.git
```

2. Launch main.py using a terminal
```bash
python main.py
```

## Explanations

To make this climate model, we first had to scale the amount of sunlight received by each latitude. After, we had to consider that earth's albedo rises when covered in snow/ice, therefore, if the average temperature of a latitude drops down below -10 C, albedo raises. Finally, we took into account those two constants : the opposite factor and the greenhouse effect.

## References

[Energy Balance Model](https://www.shodor.org/master/environmental/general/energy/index.html)

[Intransitive Model of the Earth-Atmosphere-Ocean System](https://journals.ametsoc.org/doi/pdf/10.1175/1520-0450%281972%29011%3C0004%3AAIMOTE%3E2.0.CO%3B2)


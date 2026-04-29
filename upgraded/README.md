# Gravitational Orbit Simulation

An interactive 2D simulation of the gravitational interaction between two masses using Python.

## Features
- **Real-time Physics**: Uses `scipy.integrate.solve_ivp` with the RK45 method to calculate orbital trajectories.
- **Interactive Controls**: 
  - Adjust Gravitational Constant ($G$), and masses ($M_1, M_2$) via sliders.
  - Modify the initial velocity of the second mass ($v_{x2}, v_{y2}$) on the fly.
- **Presets**:
  - **Star-Planet**: A massive central body with a smaller orbiting body.
  - **Binary Star**: Two bodies of similar mass orbiting their common center of mass.
  - **Slingshot**: A high-velocity approach resulting in a gravitational assist.
- **Visualizations**: Real-time animation showing the current position and the orbital trail of both bodies.

## Installation

### Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy matplotlib scipy
```

## Usage
Run the simulation with:
```bash
python gravitation_sim.py
```

## Credits
- Original code by Zain Ul Abideen.
- Modernized and bug-fixed by Claude Code + Gemma4.

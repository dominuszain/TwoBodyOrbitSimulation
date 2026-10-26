# Interactive orbit simulation

`gravitation_sim.py` integrates the two-body problem with
`scipy.integrate.solve_ivp` (RK45) and animates the motion in real time.

## Features

- Sliders for the gravitational constant, both masses, and the initial velocity
  of the second body.
- Presets for a star–planet system, a binary star, and a gravitational slingshot.
- Trails for both bodies and a fixed plotting window so the orbit shape is easy
  to follow.

## Run

```bash
pip install numpy scipy matplotlib
python gravitation_sim.py
```

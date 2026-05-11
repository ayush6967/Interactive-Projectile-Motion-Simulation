# Interactive Projectile Motion Simulation

A Python simulation comparing projectile trajectories with and without air resistance.

## What it does
- Models ideal projectile motion analytically using Classical Mechanics equations
- Simulates realistic projectile motion numerically using an ODE solver, accounting for air drag
- Allows user to input initial velocity, launch angle, mass, and gravitational acceleration
- Enables simulation on different planetary bodies (Moon, Mars, Jupiter etc.)
- Visualises and compares both trajectories

## Physics
Without air resistance, horizontal and vertical motion are independent — solved analytically.
With air resistance, drag couples both directions making analytical solution impossible — solved numerically.

## Output
- [Projectile Motion](projectile.png) visualaisation and Trajectory
- Range for both cases
- Maximum height reached for both cases
- Time of Flight in Both Cases

## Libraries Used
- NumPy
- Matplotlib
- SciPy

## Author
Ayush Sharma — 25MS (1st Year) BS-MS Student, IISER Kolkata

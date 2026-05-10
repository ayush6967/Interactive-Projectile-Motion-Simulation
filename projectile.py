## firstly, importing the required libraries 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

## letting the user select the conditions of the projectile motion

g = float(input("Enter gravitational acceleration in m/s^2 (Earth = 9.81): "))
v0 = float(input("Enter initial speed in m/s: "))
angle = float(input("Enter launch angle in degrees: "))
m = float(input("Enter mass of ball in kg: "))
k = 0.001

## defining important terminologies: for no drag

theta = np.radians(angle)
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)
t_flight = 2 * vy0 / g
t = np.linspace(0, t_flight, 1000)
x_no_drag = vx0 * t
y_no_drag = vy0 * t - 0.5 * g * t**2

## defining important terminologies: for with drag

def equations(t, state):
    x, y, vx, vy = state
    speed = np.sqrt(vx**2 + vy**2)
    ax = -(k/m) * speed * vx
    ay = -g - (k/m) * speed * vy
    return [vx, vy, ax, ay]

## telling the solver when to stop

def hit_ground(t, state):
    return state[1]

hit_ground.terminal = True
hit_ground.direction = -1

## running the calculations

t_max = 3 * (2 * vy0 / g)

sol = solve_ivp(
    equations,
    [0, t_max],
    [0, 0, vx0, vy0],
    events=hit_ground,
    max_step=0.01,
    dense_output=True
)

x_drag = sol.y[0]
y_drag = sol.y[1]

t_without_drag = (2*vy0)/g
t_with_drag = t_max

## plotting the trajectory

plt.figure(figsize=(10, 5))
plt.plot(x_no_drag, y_no_drag, label="Without Air Resistance", linewidth=2, color="steelblue")
plt.plot(x_drag, y_drag, label="With Air Resistance", linewidth=2, linestyle="--", color="darkorange")

plt.title("Projectile Motion: With vs Without Air Resistance")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.ylim(bottom=0)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

## showing the results

print(f"Without drag — Range: {x_no_drag[-1]:.2f} m | Max Height: {max(y_no_drag):.2f} m")
print(f"With drag    — Range: {x_drag[-1]:.2f} m  | Max Height: {max(y_drag):.2f} m")
print(f"Without drag    — Time of Flight: {t_without_drag[-1]:.2f} /sec")
print(f"With drag    — Time of Flight: {t_with_drag[-1]:.2f} /sec")

## end of the code
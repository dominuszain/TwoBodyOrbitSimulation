import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation


class GravitationSim:
    def __init__(self):
        # Physics constants and simulation limits
        self.g = 2.0
        self.m1 = 500.0
        self.m2 = 1.0
        self.stepsize = 0.1
        self.upperlimit = 1000.0

        # Initial conditions: [x1, y1, x2, y2, vx1, vy1, vx2, vy2]
        self.xo = np.array([100.0, 100.0, 100.0, 0.0, 0.0, 0.0, 0.5, 0.0])
        self._updating_presets = False

        self._setup_ui()
        self.solve()

        self.ani = FuncAnimation(
            self.fig, self.animate, frames=len(self.t_eval),
            interval=20, blit=True, repeat=True
        )

    def _setup_ui(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(left=0.25)

        self.ax.set_aspect("equal")
        self.ax.grid(True)
        self.ax.set_xlabel("X Position")
        self.ax.set_ylabel("Y Position")
        self.ax.set_autoscale_on(False)
        self.fig.suptitle("Code of Zain Ul Abideen\nModernized by Claude Code + Gemma4", fontsize=16)

        # Animation elements
        self.trail1, = self.ax.plot([], [], "-", color="blue", alpha=0.5, label="Mass 1")
        self.trail2, = self.ax.plot([], [], "-", color="red", alpha=0.5, label="Mass 2")
        self.head1, = self.ax.plot([], [], "bo", markersize=6)
        self.head2, = self.ax.plot([], [], "ro", markersize=6)
        self.ax.legend(loc="upper right")

        # Sliders configuration
        slider_configs = [
            ("G", 0.1, 5.0, self.g, [0.05, 0.70]),
            ("M1", 1.0, 1000.0, self.m1, [0.05, 0.65]),
            ("M2", 0.1, 100.0, self.m2, [0.05, 0.60]),
            ("v_x2", -2.0, 2.0, self.xo[6], [0.05, 0.55]),
            ("v_y2", -2.0, 2.0, self.xo[7], [0.05, 0.50]),
        ]

        self.sliders = {}
        for name, start, end, val, pos in slider_configs:
            ax = plt.axes([pos[0], pos[1], 0.15, 0.03])
            slider = Slider(ax, name, start, end, valinit=val)
            slider.on_changed(self.update_params)
            self.sliders[name] = slider

        # Buttons configuration
        btn_configs = [
            ("Star-Planet", self.set_massive_preset, [0.05, 0.38]),
            ("Binary Star", self.set_binary_preset, [0.05, 0.33]),
            ("Slingshot", self.set_slingshot_preset, [0.05, 0.28]),
        ]

        self.buttons = []
        for label, func, pos in btn_configs:
            ax = plt.axes([pos[0], pos[1], 0.15, 0.04])
            btn = Button(ax, label, color="lightgrey")
            btn.on_clicked(func)
            self.buttons.append(btn)

    def grav_derivatives(self, t, y):
        x1, y1, x2, y2, vx1, vy1, vx2, vy2 = y
        dx, dy = x2 - x1, y2 - y1
        dist_cubed = (dx**2 + dy**2)**1.5

        ax1, ay1 = self.g * self.m2 * dx / dist_cubed, self.g * self.m2 * dy / dist_cubed
        ax2, ay2 = -self.g * self.m1 * dx / dist_cubed, -self.g * self.m1 * dy / dist_cubed

        return [vx1, vy1, vx2, vy2, ax1, ay1, ax2, ay2]

    def solve(self):
        t_span = (0, self.upperlimit)
        self.t_eval = np.arange(0, self.upperlimit, self.stepsize)
        sol = solve_ivp(self.grav_derivatives, t_span, self.xo, t_eval=self.t_eval, method="RK45", rtol=1e-6, atol=1e-9)
        self.sol_y = sol.y
        self.ax.set_xlim(-200, 200)
        self.ax.set_ylim(-200, 200)

    def update_params(self, val):
        self.g = self.sliders["G"].val
        self.m1 = self.sliders["M1"].val
        self.m2 = self.sliders["M2"].val

        if not self._updating_presets:
            self.xo[6] = self.sliders["v_x2"].val
            self.xo[7] = self.sliders["v_y2"].val

        self._refresh_simulation()

    def _refresh_simulation(self):
        self.solve()
        self.animate(0)
        self.fig.canvas.draw_idle()

    def _apply_preset(self, g, m1, m2, xo):
        self._updating_presets = True
        self.sliders["G"].set_val(g)
        self.sliders["M1"].set_val(m1)
        self.sliders["M2"].set_val(m2)
        self.xo = np.array(xo)
        self.sliders["v_x2"].set_val(self.xo[6])
        self.sliders["v_y2"].set_val(self.xo[7])
        self._refresh_simulation()
        self._updating_presets = False

    def set_massive_preset(self, event):
        self._apply_preset(2.0, 500.0, 1.0, [0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 2.0])

    def set_binary_preset(self, event):
        self._apply_preset(2.0, 100.0, 100.0, [-50.0, 0.0, 50.0, 0.0, 0.0, -0.5, 0.0, 0.5])

    def set_slingshot_preset(self, event):
        self._apply_preset(2.0, 1000.0, 1.0, [0.0, 0.0, -150.0, 50.0, 0.0, 0.0, 1.5, 0.0])

    def animate(self, i):
        num_frames = self.sol_y.shape[1]
        i = i % num_frames
        self.trail1.set_data(self.sol_y[0, :i], self.sol_y[1, :i])
        self.trail2.set_data(self.sol_y[2, :i], self.sol_y[3, :i])
        self.head1.set_data([self.sol_y[0, i]], [self.sol_y[1, i]])
        self.head2.set_data([self.sol_y[2, i]], [self.sol_y[3, i]])
        return self.trail1, self.trail2, self.head1, self.head2

    def show(self):
        plt.show()


if __name__ == "__main__":
    GravitationSim().show()

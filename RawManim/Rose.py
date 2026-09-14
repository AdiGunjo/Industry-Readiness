from manim import *
import numpy as np

config.pixel_width = 720
config.pixel_height = 1280
config.frame_width = 8
config.frame_height = 14.2222
config.background_color = BLACK


class RoseForYou(ThreeDScene):

    @staticmethod
    def rose_point(x, theta):
        phi = (PI / 2) * np.exp(-theta / (8 * PI))

        X = 1 - 0.5 * (
            (5 / 4) *
            (1 - np.mod(3.6 * theta, 2 * PI) / PI) ** 2
            - 1 / 4
        ) ** 2

        y = (
            1.95653
            * x ** 2
            * (1.27689 * x - 1) ** 2
            * np.sin(phi)
        )

        r = X * (
            x * np.sin(phi)
            + y * np.cos(phi)
        )

        return np.array([
            r * np.sin(theta),
            r * np.cos(theta),
            X * (
                x * np.cos(phi)
                - y * np.sin(phi)
            ),
        ])

    def construct(self):

        self.set_camera_orientation(
            phi=62 * DEGREES,
            theta=-55 * DEGREES,
            gamma=0 * DEGREES,
            zoom=1.0,
        )

        title = Text(
            "Rose",
            font="Times New Roman",
            font_size=43,
            color="#F1265B",
        )
        title.to_edge(UP, buff=0.55)

        phi_eq = MathTex(
            r"\varphi(\theta)"
            r"="
            r"\frac{\pi}{2}"
            r"e^{-\theta/(8\pi)},",
            color="#E5AE58",
            font_size=31,
        )
        phi_eq.move_to([0, -4.05, 0])

        x_eq = MathTex(
            r"X(\theta)"
            r"="
            r"1-\frac12"
            r"\left("
            r"\frac54"
            r"\left("
            r"1-\frac{\theta\bmod 2\pi}{\pi}"
            r"\right)^2"
            r"-\frac14"
            r"\right)^2,",
            color="#D99862",
            font_size=27,
        )
        x_eq.move_to([0, -5.25, 0])

        xyz_eq = MathTex(
            r"(x,y,z)"
            r"="
            r"\left("
            r"r\sin\theta,"
            r"\ r\cos\theta,"
            r"\ X(x\cos\varphi-y\sin\varphi)"
            r"\right)",
            color="#E57A78",
            font_size=28,
        )
        xyz_eq.move_to([0, -6.35, 0])

        self.add_fixed_in_frame_mobjects(
            title,
            phi_eq,
            x_eq,
            xyz_eq,
        )

        self.add(
            title,
            phi_eq,
            x_eq,
            xyz_eq,
        )


        axes = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[-2.5, 2.5, 1],
            x_length=6.3,
            y_length=6.3,
            z_length=6.3,
            axis_config={
                "color": WHITE,
                "stroke_width": 1.0,
                "include_ticks": True,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            },
        )

        self.add(axes)

        rose = Surface(
            lambda x, theta: self.rose_point(x, theta),
            u_range=[0, 1],
            v_range=[-2 * PI, 15 * PI],
            resolution=(32, 220),
            fill_color="#F02258",
            fill_opacity=0.92,
            checkerboard_colors=False,
            stroke_color="#E7A83D",
            stroke_width=0.32,
        )

  
        rose.scale(2.55)

        self.play(
            Create(rose),
            run_time=2.0,
            rate_func=smooth,
        )


        self.begin_ambient_camera_rotation(
            rate=0.10,
            about="theta",
        )

        self.wait(13.7)

        self.stop_ambient_camera_rotation()

        self.wait(0.3)

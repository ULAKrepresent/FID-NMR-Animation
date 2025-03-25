import numpy as np
from manim import *

# Color definition
LIGHT_ORANGE = "#FFA500"
TMAVO_MODRA = "#15d3ee"
PURE_RED = "#f30505"

class TwoDAxesScene(Scene):
    def construct(self):
        number_text = lambda num: Tex(str(num), font_size=10)
    
        axes = Axes(
            x_range=[0, 3500, 500],
            y_range=[-90, 90, 20],
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": UP},
            x_length=10,
            y_length=6
        )
        x_label = axes.get_x_axis_label(Tex("Relaxation Time", font_size=35)).move_to(axes.c2p(3000, -11))
        y_label = axes.get_y_axis_label(Tex("Signal Strength", font_size=35)).move_to(axes.c2p(0, 95))
        
        self.play(Create(axes), run_time=3)
        self.play(Write(x_label), Write(y_label), run_time=3)
        self.wait(1)
        
        # Parameter definition
        A = 80                # amplitude
        omega = (20 * TAU) / 3500   # frequency
        T2 = 500             # konštanta tlmenia
        
        # Damped sinusoid: f(t)=A*cos(omega*t)*exp(-t/T2)
        damped_sine = axes.plot(
            lambda t: A * np.cos(omega * t) * np.exp(-t / T2),
            x_range=[0, 3500],
           color=WHITE
        ).set_stroke(width=4)
        
        # Envelope: A * exp(-t/T2)
        envelope = axes.plot(
            lambda t: A * np.exp(-t / T2),
            x_range=[0, 3500],
            color=PURE_RED
        ).set_stroke(width=4)
        
        # Equation: S(t) = A*cos(omega*t)*exp(-t/T2)
        equation = MathTex(r"S(t) = A \cos(\omega t) \exp\left(-\frac{t}{T2}\right)").move_to(axes.c2p(1750, 45))
        
        self.play(Create(damped_sine), Create(envelope), Write(equation), run_time=10)
        self.wait(1)
        self.play(FadeOut(equation))

        # Envelope segments highlight
        highlight_t1 = axes.plot(
            lambda t: A * np.exp(-t / T2),
            x_range=[100, 250],
            color=TMAVO_MODRA
        ).set_stroke(width=4)

        highlight_t2 = axes.plot(
            lambda t: A * np.exp(-t / T2),
            x_range=[450, 700],
            color=TMAVO_MODRA
        ).set_stroke(width=4)

        highlight_t3 = axes.plot(
            lambda t: A * np.exp(-t / T2),
            x_range=[2000, 2400],
            color=TMAVO_MODRA
        ).set_stroke(width=4)

        # Text
        text_t1 = Tex(r"\textbf{S} - Crystal + Amorphous phase", font_size=35).move_to(axes.c2p(1120, 60))
        text_t2 = Tex(r"\textbf{L} - Amorphous phase", font_size=35).move_to(axes.c2p(1200, 33))
        text_t3 = Tex(r"\textbf{R} - Signal residue", font_size=35).move_to(axes.c2p(2600, 10))
        # Animation
        self.play(Create(highlight_t1), Write(text_t1), run_time=2)
        self.play(Create(highlight_t2), Write(text_t2), run_time=2)
        self.play(Create(highlight_t3), Write(text_t3), run_time=2)
        self.wait(1)
        # Transformation of the equation
        equation_final = MathTex(r"\text{SR}_{w_{\text{cr}}} \, (\%) = \frac{f\cdot (\textbf{S} - \textbf{R}) - (\textbf{L} - \textbf{R})}{f\cdot (\textbf{S} - \textbf{R})}\cdot100",font_size=40).move_to(axes.c2p(2000, 50))
        text_metoda = Tex(r"\textbf{\textit{SFC} Solid Fat Content Method}", font_size=45).move_to(axes.c2p(2000, 95))
        self.play(Transform(VGroup(text_t1, text_t2, text_t3), equation_final),Write(text_metoda), run_time=3)
        self.wait(3)




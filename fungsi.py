from manim import *

class MyAnimation(Scene):
    def construct(self):
        # Membuat objek
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=1, color=RED)

        # Menampilkan objek
        self.play(circle)
        self.wait(1)
        self.play(Transform(circle, square))
        self.wait(1)
        self.play(FadeOut(circle))

        self.wait(1)


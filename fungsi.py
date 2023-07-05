from manim import *

class fungsi(Scene):
    def construct(self):
        judul = Text('Fungsi')

        self.play(Write(judul))

if __name__ == "__main__":
    scene = fungsi()
    scene.render()

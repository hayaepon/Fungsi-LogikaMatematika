from manim import *

class Page1(Scene):
    def construct(self):
        # Tampilkan konten halaman 1
        # Judul
        title1 = Tex("Fungsi Logika Matematika")
        title1.scale(1.5)
        title1.move_to(ORIGIN)
        self.play(Write(title1))

        # Garis horizontal
        line = Line(start=LEFT, end=RIGHT)
        line.next_to(title1, DOWN)
        self.play(Write(line))
        self.wait()
        
        self.play(FadeOut(title1), FadeOut(line))
        self.wait(1)

        
        # Tampilkan konten halaman 2
        # Judul
        title2 = Tex("Definisi fungsi")
        title2.scale(1.5)
        title2.to_edge(UP)
        self.play(Write(title2))

        # Garis horizontal
        line = Line(start=LEFT, end=RIGHT)
        line.next_to(title2, DOWN)
        self.play(Write(line))
        
       # Menampilkan teks definisi fungsi
        definition = Text(
            "Fungsi adalah suatu aturan yang memetakan setiap elemen dari satu himpunan ke elemen lainnya.",
            font_size=18
        )
        definition.next_to(line, DOWN, buff=0.5)
        self.play(FadeIn(definition))
        self.wait(1)

        definitionxx = Text(
            "Nama lain dari fungsi adalah pemetaan atau transformasi.",
            font_size=18
        )
        definitionxx.next_to(definition, DOWN, buff=0.5)
        self.play(FadeIn(definitionxx))
        self.wait(1)

        # Menampilkan contoh definisi fungsi
        example_title = Text("Contoh:", font_size=32)
        example_title.next_to(definitionxx, DOWN, buff=0.5)
        self.play(Write(example_title))
        self.wait(1)

        example_text = Text(
            "Fungsi kuadrat: f(x) = x^2",
            font_size=24
        )
        example_text.next_to(example_title, DOWN, buff=0.5)
        self.play(Write(example_text))
        self.wait(2)

        # Menghilangkan semua teks
        self.play(FadeOut(title2), FadeOut(line), FadeOut(definition), FadeOut(definitionxx), FadeOut(example_title), FadeOut(example_text))
        self.wait(1)

        # Membuat grid
        axes1 = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
        )

        # Fungsi awal
        function_graph1 = axes1.plot(lambda x: x**2, color=GREEN)

        # Fungsi hasil pemetaan
        mapped_graph = axes1.plot(lambda x: (x - 1)**2 + 2, color=RED)

        # Label sumbu-x
        axes_labels1 = axes1.get_axis_labels(x_label="x", y_label="y")

        # Objek teks
        equation11 = MathTex("y = x^2").to_corner(UL)
        equation21 = MathTex("y = (x - 1)^2 + 2").to_corner(UL)

        # Animasi
        self.play(Create(axes1), Write(axes_labels1))
        self.play(Create(function_graph1), Write(equation11))
        self.wait(1)
        self.play(Transform(function_graph1, mapped_graph), Transform(equation11, equation21))
        self.wait(2)

         # Menghilangkan semua teks
        self.play(FadeOut(axes1), FadeOut(function_graph1), FadeOut(mapped_graph), FadeOut(axes_labels1), FadeOut(equation11), FadeOut(equation21))
        self.wait(1)
       
        # Tampilkan konten halaman 3
        # Judul
        title3 = Tex("Jenis-jenis Fungsi")
        title3.scale(1.5)
        title3.to_edge(UP)
        self.play(Write(title3))

        # Garis horizontal
        line = Line(start=LEFT, end=RIGHT)
        line.next_to(title3, DOWN)
        self.play(Write(line))
        self.wait()
        
        textq = Tex("1.) One to One (Injektif)")
        textq.next_to(line, DOWN,)
        self.play(Write(textq))

        textw = Tex("2.) ONTO (Surjektif)")
        textw.next_to(textq, DOWN)
        self.play(Write(textw))

        texte = Tex("3.) Korespondensi Satu Ke Satu (Bijeksi / Bijection)")
        texte.next_to(textw, DOWN)
        self.play(Write(texte))
        
        textr = Tex("4.) Fungsi Konstan")
        textr.next_to(texte, DOWN)
        self.play(Write(textr))
        
        # texte = Tex("Ridho Fitra Palasa - 2110059")
        # texte.next_to(textd, DOWN)
        # self.play(Write(texte))

        self.wait(1)
        
        self.play(FadeOut(title3), FadeOut(line), FadeOut(textq), FadeOut(textw), FadeOut(texte), FadeOut(textr))
        self.wait(1)
        
        # Tampilkan konten halaman 4
        # Judul
        title4 = Tex("Fungsi Invers")
        title4.scale(1.5)
        title4.to_edge(UP)
        self.play(Write(title4))

        # Garis horizontal
        line = Line(start=LEFT, end=RIGHT)
        line.next_to(title4, DOWN)
        self.play(Write(line))
        
        # Menampilkan teks penjelasan
        text0 = Tex("Fungsi invers atau fungsi kebalikan merupakan suatu fungsi yang berkebalikan dari fungsi asalnya.",
                    font_size=30
                    )
        text0.next_to(line, DOWN,)
        self.play(Write(text0))

        text1 = Tex("Misalkan $f$ adalah fungsi dari himpunan $A$ ke himpunan $B$.",
                    font_size=30
                    )
        text1.next_to(text0, DOWN)
        self.play(Write(text1))

        text2 = Tex("Fungsi $f$ dapat direpresentasikan menggunakan diagram panah:",
                    font_size=30
                    )
        text2.next_to(text1, DOWN)
        self.play(Write(text2))

        self.wait(1)

        # Menghilangkan semua teks
        self.play(FadeOut(title4), FadeOut(line), FadeOut(text0), FadeOut(text1), FadeOut(text2))
        self.wait(1)

        # Membuat grid
        axes = Axes(
            x_range=[0, 5, 1],  # Batasi rentang x hanya pada nilai non-negatif
            y_range=[0, 5, 1],
            axis_config={"color": BLUE},
        )

        # Fungsi awal
        function_graph = axes.plot(lambda x: x**2, color=GREEN)

        # Fungsi invers
        inverse_graph = axes.plot(lambda x: np.sqrt(x), color=RED)

        # Label sumbu-x
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Objek teks
        equation1 = MathTex("y = x^2").to_corner(UL)
        equation2 = MathTex("y = \sqrt{x}").to_corner(UL)

        # Animasi
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(function_graph), Write(equation1))
        self.wait(1)
        self.play(Transform(function_graph, inverse_graph), Transform(equation1, equation2))
        self.wait(2)

       # Menghilangkan semua teks
        self.play(FadeOut(axes), FadeOut(function_graph), FadeOut(inverse_graph), FadeOut(axes_labels), FadeOut(equation1), FadeOut(equation2))
        self.wait(1)


        # Tampilkan konten halaman 5
        title5 = Tex("Kelompok 2")
        title5.scale(1.5)
        title5.to_edge(UP)
        self.play(Write(title5))
        
        # Garis horizontal
        line = Line(start=LEFT, end=RIGHT)
        line.next_to(title5, DOWN)
        self.play(Write(line))
        
        texta = Tex("Anita Meliyanti - 2110018")
        texta.next_to(line, DOWN,)
        self.play(Write(texta))

        textb = Tex("Hayatun Nufus - 2110204")
        textb.next_to(texta, DOWN)
        self.play(Write(textb))

        textc = Tex("Humaidi Fikri - 2110220")
        textc.next_to(textb, DOWN)
        self.play(Write(textc))
        
        textd = Tex("Nurul Awal Delly Murti - 2110040")
        textd.next_to(textc, DOWN)
        self.play(Write(textd))
        
        texte = Tex("Ridho Fitra Palasa - 2110059")
        texte.next_to(textd, DOWN)
        self.play(Write(texte))

        self.wait(1)
        
        # Menghilangkan semua teks
        self.play(FadeOut(title5), FadeOut(line), FadeOut(texta), FadeOut(textb), FadeOut(textc), FadeOut(textd), FadeOut(texte))
        self.wait(1)

# # Inisialisasi Manim
# if __name__ == "__main__":
#     scene = Page1()
#     scene.render()

#     scene = Page2()
#     scene.render()

#     scene = Page3()
#     scene.render()

#     scene = Page4()
#     scene.render()

#     scene = Page5()
#     scene.render()

# class Presentation(Scene):
#     def construct(self):
#         pages = [Page1(), Page2(), Page3()]

#         for page in pages:
#             self.add(page)
#             self.wait()

# Presentation().render()
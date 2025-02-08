# from manim import *

# class PhotosynthesisScene(Scene):
#     def construct(self):
#         # Title
#         title = Text("Photosynthesis", font_size=48)
#         self.play(Write(title))
#         self.wait(1)
#         self.play(FadeOut(title))
        
#         # Explanation of Photosynthesis
#         text1 = Text("Photosynthesis is the process by which plants make their food.", font_size=24)
#         text1.to_edge(UP)
#         self.play(Write(text1))
#         self.wait(2)
        
#         # Illustrating Photosynthesis
#         # Light Reaction
#         light_reaction = Text("Light Reaction in Thylakoid Membranes", font_size=20)
#         light_reaction.to_edge(LEFT)
#         self.play(Write(light_reaction))
#         self.wait(2)
#         self.play(FadeOut(light_reaction))
        
#         # Calvin Cycle
#         calvin_cycle = Text("Calvin Cycle in Stroma", font_size=20)
#         calvin_cycle.to_edge(RIGHT)
#         self.play(Write(calvin_cycle))
#         self.wait(2)
#         self.play(FadeOut(calvin_cycle))
        
#     def animate(self):
#         # Animation of light reaction
#         light_reaction = Text("Light Reaction in Thylakoid Membranes", font_size=20)
#         self.play(FadeIn(light_reaction))
        
#         # Animation of Calvin cycle
#         calvin_cycle = Text("Calvin Cycle in Stroma", font_size=20)
#         self.play(FadeIn(calvin_cycle))

# if __name__ == "__main__":
#     scene = PhotosynthesisScene()
#     scene.render()

class PhotosynthesisScene(Scene):
    def construct(self):
        # Title
        title = Text("Photosynthesis", font_size=48)
        self.play(Write(title))
        self.wait(1)

        # Explanation of Photosynthesis
        text1 = Text("Photosynthesis is the process by which plants make their food.", font_size=24)
        text1.to_edge(UP)
        self.play(Write(text1))
        self.wait(2)

        # Illustrating Photosynthesis
        light_reaction = Text("Light Reaction in Thylakoid Membranes", font_size=20)
        light_reaction.to_edge(LEFT)
        self.play(Write(light_reaction))
        self.wait(2)
        self.play(FadeOut(light_reaction))

        calvin_cycle = Text("Calvin Cycle in Stroma", font_size=20)
        calvin_cycle.to_edge(RIGHT)
        self.play(Write(calvin_cycle))
        self.wait(2)
        self.play(FadeOut(calvin_cycle))
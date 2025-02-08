# # from manim import *
# # from langchain.tools import tool
# # from langchain_community.llms import OpenAI, Ollama
# # import os

# # # Set the API key for OpenAI
# # os.environ["OPENAI_API_KEY"] = "NA"

# # class SceneGeneratorTool:
# #     def __init__(self):
# #         self.llm = Ollama(
# #             model="gemma:2b",
# #             base_url="http://localhost:11434",
# #         )
    
# #     @tool("This tool generates a Manim scene definition for a given concept from agent 1.")
# #     def generate_scene_definition(self, concept: str) -> str:
# #         """
# #         Generates a Manim scene definition for a given concept.

# #         Args:
# #             concept (str): The concept to generate the scene definition for.

# #         Returns:
# #             str: The scene definition script.
# #         """
# #         prompt = f"""
# #         Create a Manim scene definition to explain the concept of "{concept}". The scene should include a title, an explanation text, and a visual representation of the concept.

# #         Example:

# #         # Title
# #         title = Text('{concept}', font_size=48)
# #         self.play(Write(title))
# #         self.wait(1)
# #         self.play(FadeOut(title))

# #         # Explanation of {concept}
# #         text1 = Text('{concept} is ...', font_size=24)
# #         text1.to_edge(UP)
# #         self.play(Write(text1))
# #         self.wait(2)

# #         # Illustrating {concept}
# #         ...
# #         """
# #         try:
# #             response = self.llm.generate(prompt)
# #             return response['choices'][0]['text'].strip()  # Strip to remove extra spaces/newlines
# #         except Exception as e:
# #             print(f"Error generating scene definition: {e}")
# #             return ""

# #     @tool("This tool saves the generated Manim script to a Python file.")
# #     def save_manim_script(self, concept: str):
# #         """
# #         Saves the generated Manim script to a .py file.

# #         Args:
# #             concept (str): The concept to generate the scene definition for.

# #         Returns:
# #             str: The path to the saved Python script file.
# #         """
# #         scene_definition = self.generate_scene_definition(concept)
        
# #         # Define the output file path
# #         script_path = os.path.join(
# #             r'C:\Users\PC\Desktop\taj\starter_template\tools',
# #             f'{concept.replace(" ", "_")}_scene.py'
# #         )

# #         if not scene_definition:
# #             print("No scene definition generated. Script not created.")
# #             return None

# #         try:
# #             # Write the Manim scene definition to the Python script file
# #             with open(script_path, 'w') as script_file:
# #                 script_file.write(f"from manim import *\n\n")
# #                 script_file.write(f"class {concept.replace(' ', '')}Scene(Scene):\n")
# #                 script_file.write(f"    def construct(self):\n")
# #                 script_file.write(f"        {scene_definition}\n")

# #             print(f"Manim script for {concept} created and saved to {script_path}")
# #             return script_path
# #         except Exception as e:
# #             print(f"Error creating Manim script: {e}")
# #             return None
# # scene_generator_tool.py

# from manim import *
# from langchain.tools import tool
# import requests
# import os
# import logging

# # Set up logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)

# class SceneGeneratorTool:
#     def __init__(self, api_url: str, output_dir: str = None):
#         """
#         Initialize the SceneGeneratorTool with an output directory for generated scripts.

#         Args:
#             api_url (str): The API endpoint of the fine-tuned model running in Colab.
#             output_dir (str, optional): Directory where Manim scripts will be saved.
#                                         Defaults to a "manim_scripts" folder in the current directory.
#         """
#         self.api_url = api_url  # Colab API URL for your fine-tuned model

#         if output_dir is None:
#             output_dir = os.path.join(os.getcwd(), "manim_scripts")
#         self.output_dir = output_dir
#         os.makedirs(self.output_dir, exist_ok=True)

#         logger.info(f"SceneGeneratorTool initialized with output directory: {self.output_dir} and API URL: {self.api_url}")

#     @tool("Generate a Manim scene definition for a given concept from agent input.")
#     def generate_scene_definition(self, concept: str) -> str:
#         """
#         Generate a Manim scene definition script for the given concept.

#         Args:
#             concept (str): The concept for which to generate the scene.

#         Returns:
#             str: The generated scene definition script.
#         """
#         prompt = f"""
#         Create a Manim scene definition to explain the concept of "{concept}". The scene should include a title, 
#         an explanation text, and a visual representation of the concept.

#         Example:

#         # Title
#         title = Text('{concept}', font_size=48)
#         self.play(Write(title))
#         self.wait(1)
#         self.play(FadeOut(title))

#         # Explanation of {concept}
#         text1 = Text('{concept} is ...', font_size=24)
#         text1.to_edge(UP)
#         self.play(Write(text1))
#         self.wait(2)

#         # Illustrating {concept}
#         ...
#         """

#         try:
#             response = requests.post(self.api_url, json={"prompt": prompt})
#             response.raise_for_status()  # Raise an error if the request fails
#             scene_definition = response.json().get("text", "").strip()

#             if not scene_definition:
#                 logger.warning("Received an empty scene definition from the model.")
#                 return ""

#             logger.info(f"Scene definition generated for concept: {concept}")
#             return scene_definition
#         except Exception as e:
#             logger.error(f"Error generating scene definition for {concept}: {e}")
#             return ""

#     @tool("Save the generated Manim script to a Python file.")
#     def save_manim_script(self, concept: str) -> str:
#         """
#         Save the generated Manim scene definition as a Python script file.

#         Args:
#             concept (str): The concept for which the scene is generated.

#         Returns:
#             str: The path to the saved script file, or None if an error occurred.
#         """
#         scene_definition = self.generate_scene_definition(concept)
#         if not scene_definition:
#             logger.error("No scene definition generated. Script not created.")
#             return None

#         # Create a safe filename based on the concept
#         filename = f"{concept.replace(' ', '_')}_scene.py"
#         script_path = os.path.join(self.output_dir, filename)

#         try:
#             with open(script_path, 'w') as script_file:
#                 script_file.write("from manim import *\n\n")
#                 script_file.write(f"class {concept.replace(' ', '')}Scene(Scene):\n")
#                 script_file.write("    def construct(self):\n")
#                 script_file.write("        " + scene_definition.replace("\n", "\n        ") + "\n")

#             logger.info(f"Manim script for {concept} created and saved to {script_path}")
#             return script_path
#         except Exception as e:
#             logger.error(f"Error creating Manim script for {concept}: {e}")
#             return None





# from manim import *
# from langchain.tools import tool
# from langchain_community.llms import OpenAI, Ollama
# import os

# # Set the API key for OpenAI
# os.environ["OPENAI_API_KEY"] = "NA"

# class SceneGeneratorTool:
#     def __init__(self):
#         self.llm = Ollama(
#             model="gemma:2b",
#             base_url="http://localhost:11434",
#         )
    
#     @tool("This tool generates a Manim scene definition for a given concept from agent 1.")
#     def generate_scene_definition(self, concept: str) -> str:
#         """
#         Generates a Manim scene definition for a given concept.

#         Args:
#             concept (str): The concept to generate the scene definition for.

#         Returns:
#             str: The scene definition script.
#         """
#         prompt = f"""
#         Create a Manim scene definition to explain the concept of "{concept}". The scene should include a title, an explanation text, and a visual representation of the concept.

#         Example:

#         # Title
#         title = Text('{concept}', font_size=48)
#         self.play(Write(title))
#         self.wait(1)
#         self.play(FadeOut(title))

#         # Explanation of {concept}
#         text1 = Text('{concept} is ...', font_size=24)
#         text1.to_edge(UP)
#         self.play(Write(text1))
#         self.wait(2)

#         # Illustrating {concept}
#         ...
#         """
#         try:
#             response = self.llm.generate(prompt)
#             return response['choices'][0]['text'].strip()  # Strip to remove extra spaces/newlines
#         except Exception as e:
#             print(f"Error generating scene definition: {e}")
#             return ""

#     @tool("This tool saves the generated Manim script to a Python file.")
#     def save_manim_script(self, concept: str):
#         """
#         Saves the generated Manim script to a .py file.

#         Args:
#             concept (str): The concept to generate the scene definition for.

#         Returns:
#             str: The path to the saved Python script file.
#         """
#         scene_definition = self.generate_scene_definition(concept)
        
#         # Define the output file path
#         script_path = os.path.join(
#             r'C:\Users\PC\Desktop\taj\starter_template\tools',
#             f'{concept.replace(" ", "_")}_scene.py'
#         )

#         if not scene_definition:
#             print("No scene definition generated. Script not created.")
#             return None

#         try:
#             # Write the Manim scene definition to the Python script file
#             with open(script_path, 'w') as script_file:
#                 script_file.write(f"from manim import *\n\n")
#                 script_file.write(f"class {concept.replace(' ', '')}Scene(Scene):\n")
#                 script_file.write(f"    def construct(self):\n")
#                 script_file.write(f"        {scene_definition}\n")

#             print(f"Manim script for {concept} created and saved to {script_path}")
#             return script_path
#         except Exception as e:
#             print(f"Error creating Manim script: {e}")
#             return None
# scene_generator_tool.py



# from manim import *
from langchain.tools import tool
import requests
import os
import logging
from typing import Optional  # Import Optional
import textwrap
# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class SceneGeneratorTool:
    def __init__(self, api_url: str, output_dir: Optional[str] = None):
        """
        Initialize the SceneGeneratorTool with an output directory for generated scripts.

        Args:
            api_url (str): The API endpoint of the fine-tuned model running in Colab.
            output_dir (str, optional): Directory where Manim scripts will be saved.
                                        Defaults to a "manim_scripts" folder in the current directory.
        """
        self.api_url = "https://4b4e-34-142-235-209.ngrok-free.app" #api_url  # Colab API URL for your fine-tuned model

        # if output_dir is None:
        #     output_dir = os.path.join(os.getcwd(), "manim_scripts")
        # self.output_dir = output_dir
        # os.makedirs(self.output_dir, exist_ok=True) 
        self.output_dir = output_dir or os.path.join(os.getcwd(), "manim_scripts")
        os.makedirs(self.output_dir, exist_ok=True)

        logger.info(f"SceneGeneratorTool initialized with output directory: {self.output_dir} and API URL: {self.api_url}")

    @tool("Generate a Manim scene definition for a given concept from agent input.")
    def generate_scene_definition(self, concept: str) -> str:
        """
        Generate a Manim scene definition script for the given concept with minimum 8-minute duration.
        """
        prompt = f"""
        Create a comprehensive Manim scene definition to explain "{concept}" with minimum 8-minute runtime (480 seconds).
        Follow these strict requirements:

        1. Structural Requirements:
        - 5-7 main sections with clear transitions
        - 3-5 visualizations per major concept component
        - Multiple text explanations that persist and build on screen
        - Progressive revelation of complex diagrams

        2. Timing Guidelines:
        - Total animation time >= 480 seconds (8 minutes)
        - Minimum 3 seconds per text animation
        - Minimum 5 seconds per complex visualization build
        - 2-3 second transitions between sections
        - 2-5 second wait times after key revelations

        3. Content Requirements:
        - Start with title sequence (10-15 seconds)
        - Detailed historical context section
        - Mathematical formulation with equation animations
        - Real-world applications with diagram builds
        - Interactive elements using ValueTracker/updaters
        - Summary with persistent key points

        4. Animation Techniques:
        - Combine Write, DrawBorderThenFill, and Transform
        - Use LaggedStart for complex sequences
        - Include coordinated text/diagram reveals
        - Employ multiple camera angles/zooms
        - Use VGroups for complex system visualizations

        Example Structure:
        
        class """"{concept.replace(' ', '')}""""Scene(Scene):
            def construct(self):
                # Title Sequence (15s)
                title = Tex(r"\\textbf{{{concept}}}", font_size=72)
                subtitle = Text("A Comprehensive Explanation", font_size=36)
                self.play(LaggedStart(
                    Write(title, run_time=2),
                    FadeIn(subtitle, shift=DOWN, run_time=3),
                    lag_ratio=0.5
                ))
                self.wait(2)
                self.play(FadeOut(title, shift=UP), FadeOut(subtitle, shift=DOWN))
                self.wait(1)

                # Core Concept Breakdown (180s)
                concept_vg = VGroup()
                for i in range(5):
                    text = Text(f"Key Component i+1", font_size=24)
                    diagram = generate_component_diagram(i)
                    group = VGroup(text, diagram).arrange(DOWN)
                    concept_vg.add(group)
                
                concept_vg.arrange_in_grid(cols=2, buff=1).scale(0.8)
                self.play(FadeIn(concept_vg[0], shift=LEFT), run_time=3)
                self.wait(2)
                for i in range(1, 5):
                    self.play(
                        ReplacementTransform(concept_vg[i-1], concept_vg[i]),
                        run_time=4
                    )
                    self.wait(3)

                # Mathematical Formulation (120s)
                equation = MathTex(r"\\mathcal{{F}}(x) = \\int_{{-\\infty}}^{{\\infty}} f(t)e^{{-2\\pi ixt}} dt")
                self.play(Write(equation), run_time=5)
                self.wait(2)
                for term in equation:
                    self.play(
                        Indicate(term, color=YELLOW),
                        run_time=2
                    )
                    self.wait(1)
                
                # Real-world Applications (150s)
                apps = VGroup(*[create_application_scene(i) for i in range(3)])
                apps.arrange(RIGHT, buff=1)
                for app in apps:
                    self.play(DrawBorderThenFill(app), run_time=6)
                    self.wait(4)

                # Interactive Demonstration (60s)
                plane = NumberPlane()
                dot = Dot().move_to(plane.c2p(0,0))
                self.play(Create(plane), run_time=3)
                self.play(FadeIn(dot))
                for x in range(1,5):
                    self.play(
                        dot.animate.move_to(plane.c2p(x, x**2)),
                        run_time=2
                    )
                    self.wait(1)

                # Conclusion Sequence (45s)
                summary = BulletedList(
                    "Key Point 1",
                    "Key Point 2",
                    "Key Point 3",
                    height=4,
                    width=6
                )
                self.play(FadeIn(summary), run_time=5)
                self.wait(4)
                for item in summary:
                    self.play(Flash(item))
                    self.wait(2)
        """

        try:
            response = requests.post(
                self.api_url,
                json={
                    "prompt": prompt,
                    "temperature": 0.3,
                    "max_tokens": 2000
                }
            )
            
            if response.status_code == 200:
                return response.json().get("scene_definition", "")
            else:
                logger.error(f"API call failed: {response.status_code}")
                return ""
                
        except Exception as e:
            logger.error(f"Failed to generate scene: {e}")
            return ""

    # # Helper function to estimate duration
    # def sum_duration(code: str) -> int:
    #     # Implement duration parsing logic here
    #     return estimated_seconds

    # def _generate_extension(self, existing_code: str) -> str:
    #     """Generate additional content to meet duration requirements"""
    #     extension_prompt = f"""
    #     Add 120 seconds to this scene while maintaining coherence:
    #     {existing_code}
        
    #     Extension strategies:
    #     - Add detailed case study
    #     - Include common misconceptions
    #     - Create comparative diagrams
    #     - Add interactive quiz elements
    #     - Include historical timeline
    #     - Develop practical examples
    #     """
    #     # Call API to generate extension
    #     return extension_code
# from crewai import Task
# from textwrap import dedent

# class techerTasks:
#     def __tip_section(self):
#         return "If you do your BEST WORK, I'll give you a $10,000 commission!"

#     def task_1_name(self, agent, var1, var2, age, pdf, ch):
#         return Task(
#             description=dedent(
#                 f"""
#                 Your task is to thoroughly understand the PDF book titled "{pdf}" and prepare to explain its content to a student.
                
#                 You should start by selecting appropriate teaching techniques and strategies based on the student's age ({age}) and the subject matter of the book.
                
#                 **Task Steps:**
                
#                 1. **Understand the Content:**
#                 - Read and comprehend the relevant chapter ({ch}) from the PDF book.
                
#                 2. **Plan Your Lesson:**
#                 - **Introduction:** Provide an overview of the topic and explain its importance.
#                 - **Body:** Break down the content into manageable sections. Use a variety of teaching methods to cater to different learning styles (visual, auditory, kinesthetic).
#                 - **Conclusion:** Summarize the key points and ensure the student understands the material.
                
#                 3. **Define Learning Goals:**
#                 - **Specific:** Clearly outline what the student should know or be able to do by the end of the lesson.
#                 - **Measurable:** Ensure the goals can be assessed to track progress.
#                 - **Achievable:** Set realistic goals based on the student's current level.
#                 - **Relevant:** Align the goals with the student's interests and future aspirations.
#                 - **Time-bound:** Establish a timeline for achieving these goals.
                
#                 4. **Provide Clear Explanations:**
#                 - Offer concise explanations of concepts.
#                 - Show practical examples to illustrate abstract ideas.
                
#                 5. **Use Recent Data:**
#                 - Ensure your teaching incorporates the most recent data and information available.
                
#                 6. **Utilize Multimedia:**
#                 - Work with a script editor to create Manim scripts and graphics to enhance your lecture.
                
#                 Finally, explain the selected chapter ({ch}) from the PDF book ({pdf}) using the following variables:
#                 - {var1}
#                 - {var2}
                
#                 {self.__tip_section()}
#             """
#             ),
#             agent=agent,
#             expected_output = """
#              **Lesson Overview:**

#             **Introduction:** 
#             Today, we will explore the concept of Photosynthesis. This topic is crucial as it explains how plants produce their own food using sunlight.

#             **Content Breakdown:**
#             1. **Photosynthesis Overview:** 
#             Photosynthesis is the process by which green plants, algae, and some bacteria convert light energy into chemical energy stored in glucose. It takes place primarily in the chloroplasts of plant cells.

#             2. **Steps of Photosynthesis:**
#             - **Light Reaction:** This occurs in the thylakoid membranes of the chloroplasts where sunlight is absorbed by chlorophyll and used to split water molecules into oxygen and hydrogen.
#             - **Calvin Cycle:** In the stroma of chloroplasts, the ATP and NADPH produced in the light reaction are used to convert carbon dioxide into glucose.

#             3. **Teaching Techniques:**
#             - **Visual Aids:** Use diagrams of the photosynthesis process.
#             - **Demonstration:** Simple experiments showing oxygen production in water plants.
#             - **Multimedia:** Incorporate a short video explaining photosynthesis.

#             4. **Learning Goals:**
#             - **Specific:** Students should be able to explain the basic steps of photosynthesis.
#             - **Measurable:** Students will complete a worksheet identifying the stages of photosynthesis.
#             - **Achievable:** Goals are set based on current student understanding.
#             - **Relevant:** Photosynthesis is fundamental to understanding plant biology.
#             - **Time-bound:** Goals should be achieved by the end of the lesson.

#             5. **Clear Explanations:**
#             - Photosynthesis is essential for plant growth and oxygen production. 

#             6. **Annotated Document:**
#             - **Chapter 5:** Contains key points with annotations explaining each stage of photosynthesis.

#             **Tip:** If you do your BEST WORK, I'll give you a $10,000 commission!
#             """
#         )

#     def task_2_name(self, agent, context):
#         return Task(
#             description=dedent(
#                 f"""
#                 Your task is to create a Manim script using the text and annotations from Agent 1. 
#                 You should integrate the following elements:

#                 1. **Animation and Visuals:**
#                 - Wrap the relevant text with animations that visually explain the concepts.
#                 - Use physical animations to illustrate key ideas.
#                 - Create a suitable background that helps maintain the theme of the topic and keeps students engaged.

#                 2. **Identify Learning Objectives:**
#                 - Clearly define what you want the students to learn from the animation.
#                 - Ensure the objectives are Specific, Measurable, Achievable, Relevant, and Time-bound (SMART).

#                 3. **Break Down Complex Ideas:**
#                 - Divide complex concepts into smaller, manageable parts for easier animation.
#                 - Use analogies and visuals to clarify difficult topics.

#                 4. **Storyboard:**
#                 - Outline the sequence of your script.
#                 - Plan the visuals, text, and narration for each section to maintain a logical flow.

#                 5. **Script Writing:**
#                 - Write a clear and concise script that aligns with the visuals.
#                 - Ensure the language is appropriate for the age (24) and comprehension level of your students.

#                 {self.__tip_section()}

#                 Finally, make sure to consider additional creative elements that can enhance the script and improve student engagement.
#             """
#             ),
#             agent=agent,
#             context=context,
#             expected_output = """
#             from manim import *

#             class PhotosynthesisScene(Scene):
#                 def construct(self):
#                     # Title
#                     title = Text("Photosynthesis", font_size=48)
#                     self.play(Write(title))
#                     self.wait(1)
#                     self.play(FadeOut(title))

#                     # Explanation of Photosynthesis
#                     text1 = Text("Photosynthesis is the process by which plants make their food.", font_size=24)
#                     text1.to_edge(UP)
#                     self.play(Write(text1))
#                     self.wait(2)

#                     # Illustrating Photosynthesis
#                     # Light Reaction
#                     light_reaction = Text("Light Reaction in Thylakoid Membranes", font_size=20)
#                     light_reaction.to_edge(LEFT)
#                     self.play(Write(light_reaction))
#                     self.wait(2)
#                     self.play(FadeOut(light_reaction))

#                     # Calvin Cycle
#                     calvin_cycle = Text("Calvin Cycle in Stroma", font_size=20)
#                     calvin_cycle.to_edge(RIGHT)
#                     self.play(Write(calvin_cycle))
#                     self.wait(2)
#                     self.play(FadeOut(calvin_cycle))
#             """
#         )
import textwrap
from crewai import Task
from textwrap import dedent

class techerTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2, age, pdf, ch):
        # # Dynamically adapt lesson based on age and selected chapter
        # lesson_intro = f"Your task is to thoroughly understand the PDF book titled '{pdf}' and prepare to explain its content to a student of age {age}. "
        # lesson_intro += f"Focus on chapter '{ch}' and use the following variables in your explanation: {var1} and {var2}."
        # age = int(age)
        # # Dynamically adapt teaching methods based on age
        # teaching_methods = "Teaching Methods:\n"
        # if age < 12:
        #     teaching_methods += "- Use lots of visuals and hands-on activities.\n"
        #     teaching_methods += "- Break concepts down into very simple terms.\n"
        # elif age < 18:
        #     teaching_methods += "- Use a mix of visuals and short explanations.\n"
        #     teaching_methods += "- Encourage group discussions to promote understanding.\n"
        # else:
        #     teaching_methods += "- Use advanced concepts and encourage critical thinking.\n"
        #     teaching_methods += "- Introduce real-world applications to make the material more relevant.\n"

        # # Task description that uses variables for dynamic generation
        # task_description = dedent(f"""
        # {lesson_intro}

        # **Teaching Plan:**
        # 1. **Understand the Content:**
        #     - Read and comprehend the relevant chapter ({ch}) from the PDF book.
        
        # 2. **Plan Your Lesson:**
        #     - **Introduction:** Provide an overview of the topic and explain its importance.
        #     - **Body:** Break down the content into manageable sections. {teaching_methods}
        #     - **Conclusion:** Summarize the key points and ensure the student understands the material.

        # 3. **Define Learning Goals:**
        #     - **Specific:** Clearly outline what the student should know or be able to do by the end of the lesson.
        #     - **Measurable:** Ensure the goals can be assessed to track progress.
        #     - **Achievable:** Set realistic goals based on the student's current level.
        #     - **Relevant:** Align the goals with the student's interests and future aspirations.
        #     - **Time-bound:** Establish a timeline for achieving these goals.

        # 4. **Provide Clear Explanations:**
        #     - Offer concise explanations of concepts.
        #     - Use practical examples to illustrate abstract ideas.
        
        # 5. **Utilize Multimedia:**
        #     - Consider using videos, interactive tools, or illustrations to aid understanding.

        # **Tip:** {self.__tip_section()}
        # """)
        # Dynamically adapt teaching methods based on age
        teaching_methods = self._get_teaching_methods(age)
        
        lesson_intro = f"Your task is to thoroughly understand the PDF book titled '{pdf}' and prepare to explain its content to a student of age {age}. "
        lesson_intro += f"Focus on chapter '{ch}' and use the following variables in your explanation: {var1} and {var2}."

        task_description = dedent(f"""
        {lesson_intro}

        **Teaching Plan:**
        1. **Understand the Content:**
            - Read and comprehend the relevant chapter ({ch}) from the PDF book.
        
        2. **Plan Your Lesson:**
            {teaching_methods}

        3. **Define Learning Goals:**
            - Specific: Clearly outline what the student should know or be able to do
            - Measurable: Ensure the goals can be assessed
            - Achievable: Set realistic goals based on the student's level
            - Relevant: Align with student's interests
            - Time-bound: Establish a timeline

        **Tip:** {self.__tip_section()}
        """)
        
        # Added expected_output parameter
        return Task(
            description=task_description,
            agent=agent,
            expected_output="A comprehensive lesson plan with explanation of the chapter content, teaching methods, and learning goals."
        )
    def _get_teaching_methods(self, age):
            if isinstance(age, str):
                age = int(age)
                
            if age < 12:
                return dedent("""
                    - Use lots of visuals and hands-on activities
                    - Break concepts down into very simple terms
                    - Include games and interactive elements
                """)
            elif age < 18:
                return dedent("""
                    - Use a mix of visuals and short explanations
                    - Encourage group discussions
                    - Include practical examples
                """)
            else:
                return dedent("""
                    - Use advanced concepts and critical thinking
                    - Introduce real-world applications
                    - Encourage independent research
                """)
    def task_2_name(self, agent, context):
        # Create a more flexible Manim script creation task
        task_description = dedent(f"""
        Your task is to create a Manim script using the text and annotations from Agent 1. 
        You should integrate the following elements:

        1. **Animation and Visuals:**
            - Wrap the relevant text with animations that visually explain the concepts.
            - Use physical animations to illustrate key ideas.
            - Create a suitable background that helps maintain the theme of the topic and keeps students engaged.

        2. **Identify Learning Objectives:**
            - Clearly define what you want the students to learn from the animation.
            - Ensure the objectives are Specific, Measurable, Achievable, Relevant, and Time-bound (SMART).

        3. **Break Down Complex Ideas:**
            - Divide complex concepts into smaller, manageable parts for easier animation.
            - Use analogies and visuals to clarify difficult topics.

        4. **Storyboard:**
            - Outline the sequence of your script.
            - Plan the visuals, text, and narration for each section to maintain a logical flow.

        5. **Script Writing:**
            - Write a clear and concise script that aligns with the visuals.
            - Ensure the language is appropriate for the age and comprehension level of your students.

        **Tip:** {self.__tip_section()}

        Finally, make sure to consider additional creative elements that can enhance the script and improve student engagement.
        """)
        
        return Task(
            description=task_description,
            agent=agent,
            context=context,
            expected_output = "A complete Manim script with visualizations based on the lesson content."  # Same approach here: no static output
        )

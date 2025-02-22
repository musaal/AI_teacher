import textwrap
from crewai import Task
from textwrap import dedent

class techerTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2, age, pdf, ch):

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

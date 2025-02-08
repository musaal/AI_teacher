# from crewai import Agent
# from textwrap import dedent
# from langchain_community.llms import OpenAI#, Ollama
# #######
# from langchain_ollama import OllamaLLM
# ####
# from langchain_openai import ChatOpenAI

# from tools.animation_tool import SceneGeneratorTool
# from tools.QueryEngine import PDFExtractionTools

# import os
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Ensure the OpenAI API key is set if using OpenAI services
# os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# class teachAgents:
#     def __init__(self):
#         # Uncomment and configure if you plan to use OpenAI services
#         # self.OpenAInGPT35n = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
#         # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
#         # self.Ollama = Ollama(model="openhermes")
        
#         self.llm = OllamaLLM(
#             model="deepseek-r1:1.5b ",
#             base_url="http://localhost:11434",
#         )

#     def agent_1_name(self):
#         try:
#             agent = Agent(
#                 role="Experienced Professional Teacher",
#                 backstory=dedent(
#                     """
#                     A seasoned teacher with 10 years of experience, deeply influenced by renowned science communicators 
#                     like Carl Sagan, Richard Feynman, Stephen Hawking, Neil deGrasse Tyson, and Brian Cox. 
#                     Known for exceptional communication skills, you effectively engage with students of all ages. 
#                     Famous for your work in simplifying complex subjects and authoring accessible books, 
#                     you have a strong online presence and a robust technique for delivering impactful lessons.
#                     """
#                 ),
#                 goal=dedent(
#                     """
#                     Transform your books into engaging lectures designed to teach students everything they need to know, 
#                     preparing them thoroughly for exams. Your aim is to make the learning journey enjoyable and 
#                     memorable for students, fostering a love for the subject.
#                     """
#                 ),
#                 tools=[
#                     PDFExtractionTools.extract_text_from_pdf,
#                     PDFExtractionTools.index_text,
#                     PDFExtractionTools.extract_and_index,
#                 ],
#                 allow_delegation=False,
#                 verbose=True,
#                 llm=self.llm,
#                 max_iter=2
#             )
#             logger.info("Agent 1 initialized successfully.")
#             return agent
#         except Exception as e:
#             logger.error(f"An error occurred in agent_1_name: {e}")
#             raise

#     def agent_2_name(self):
#         try:
#             agent = Agent(
#                 role="Professional Manim Script Creator",
#                 backstory=dedent(
#                     """
#                     You are an experienced professional in creating educational animations using Manim. With a strong background in 
#                     mathematics and physics, you specialize in using Manim to develop engaging, visually appealing animations. 
#                     Your work is inspired by the likes of Grant Sanderson from 3Blue1Brown, and you aim to make complex concepts 
#                     accessible to a broad audience. You have extensive experience in graphic design, programming, and animation.
#                     """
#                 ),
#                 goal=dedent(
#                     """
#                     Your goal is to produce high-quality educational animations that illustrate mathematical and physics 
#                     concepts in a clear, engaging, and visually appealing manner. Using Manim, you aim to enhance the learning 
#                     experience of students and help them grasp difficult topics through intuitive and creative visualizations.
#                     """
#                 ),
#                 tools=[
#                     SceneGeneratorTool.generate_scene_definition
#                     # SceneGeneratorTool.save_manim_script   
#                 ],
#                 allow_delegation=False,
#                 verbose=True,
#                 llm=self.llm,
#                 max_iter=2
#             )
#             logger.info("Agent 2 initialized successfully.")
#             return agent
#         except Exception as e:
#             logger.error(f"An error occurred in agent_2_name: {e}")
#             raise




from crewai import Agent, LLM
from textwrap import dedent
#from langchain_ollama import OllamaLLM
from tools.animation_tool import SceneGeneratorTool
from tools.QueryEngine import PDFExtractionTools
import os
import logging
import textwrap

# from crewai import Agent, Task, Crew

# from crewai_tools import (
#     DirectoryReadTool,
#     DOCXSearchTool,
#     SerperDevTool,
#     WebsiteSearchTool
# )

# Instantiate tools
# docs_tool = DirectoryReadTool(directory='./blog-posts')
# file_tool = DOCXSearchTool(config={"api_key": os.getenv("OPENAI_API_KEY")})
# search_tool = SerperDevTool()
# web_rag_tool = WebsiteSearchTool()


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class teachAgents:
    def __init__(self):
        # Configure the LLM with the correct provider and model
        self.llm = LLM(
            base_url="http://localhost:11434",  # Ensure this matches your Ollama server's URL
            model="ollama/deepseek-r1:1.5b",    # Prefix the model name with 'ollama/'
        )

    def agent_1_name(self):
        try:
            agent = Agent(
                role="Experienced Professional Teacher",
                backstory=dedent(
                    """
                    A seasoned teacher with 10 years of experience, deeply influenced by renowned science communicators 
                    like Carl Sagan, Richard Feynman, Stephen Hawking, Neil deGrasse Tyson, and Brian Cox. 
                    Known for exceptional communication skills, you effectively engage with students of all ages. 
                    Famous for your work in simplifying complex subjects and authoring accessible books, 
                    you have a strong online presence and a robust technique for delivering impactful lessons.
                    """
                ),
                goal=dedent(
                    """
                    Transform your books into engaging lectures designed to teach students everything they need to know, 
                    preparing them thoroughly for exams. Your aim is to make the learning journey enjoyable and 
                    memorable for students, fostering a love for the subject.
                    """
                ),
                tools=[
                    PDFExtractionTools.extract_text_from_pdf,
                    PDFExtractionTools.index_text,
                    PDFExtractionTools.extract_and_index,
                    
                ],
                allow_delegation=False,
                verbose=True,
                llm=self.llm,
                max_iter=2
            )
            logger.info("Agent 1 initialized successfully.")
            return agent
        except Exception as e:
            logger.error(f"An error occurred in agent_1_name: {e}")
            raise

    def agent_2_name(self):
        try:
            agent = Agent(
                role="Professional Manim Script Creator",
                backstory=dedent(
                    """
                    You are an experienced professional in creating educational animations using Manim. With a strong background in 
                    mathematics and physics, you specialize in using Manim to develop engaging, visually appealing animations. 
                    Your work is inspired by the likes of Grant Sanderson from 3Blue1Brown, and you aim to make complex concepts 
                    accessible to a broad audience. You have extensive experience in graphic design, programming, and animation.
                    """
                ),
                goal=dedent(
                    """
                    Your goal is to produce high-quality educational animations that illustrate mathematical and physics 
                    concepts in a clear, engaging, and visually appealing manner. Using Manim, you aim to enhance the learning 
                    experience of students and help them grasp difficult topics through intuitive and creative visualizations.
                    """
                ),
                tools=[
                    SceneGeneratorTool.generate_scene_definition
                    # SceneGeneratorTool.save_manim_script   
                ],
                allow_delegation=False,
                verbose=True,
                llm=self.llm,
                max_iter=2
            )
            logger.info("Agent 2 initialized successfully.")
            return agent
        except Exception as e:
            logger.error(f"An error occurred in agent_2_name: {e}")
            raise

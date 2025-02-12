import os
from crewai import Crew, Process
from langchain_community.llms import OpenAI , Ollama
# from langchain.llms import Ollama 
# from langchain_community.llms import Ollama 

from agents import teachAgents
from tasks import techerTasks
from tools.file_io import save_and_execute
from textwrap import dedent
import logging
import textwrap
# Load environment variables from .env file
# load_dotenv()
# from dotenv import load_dotenv
# import os

# load_dotenv()

# from langchain_ollama import OllamaLLM

# Environment variables for static file handling (if needed)
static_directory = os.getenv('STATIC_DIRECTORY', 'static')
static_route = os.getenv('STATIC_ROUTE', '/static')
static_name = os.getenv('STATIC_NAME', 'static_files')

# # Initialize the language model
llm = Ollama(
    model="deepseek-r1:1.5b ",
    base_url="http://localhost:11434"
)
# # gpt-3.5-turbo

# Path to the PDF file
pdf_path = "C:/Users/NTC/Desktop/musa/statistical mechanics _1/Ch1.pdf"

class TeachCrew:
    def __init__(self, ch, age, pdf, var1, var2):
        self.ch = ch
        self.age =  int(age) # age
        self.pdf = pdf
        self.var1 = var1
        self.var2 = var2
        # self.llm = OllamaLLM(
        #     base_url="http://localhost:11434",
        #     model="deepseek-r1:1.5b",  # Using a more suitable model
  
        # )
    def run(self):
        try:
            # Initialize agents and tasks
            agents = teachAgents()#self.llm
            tasks = techerTasks()

            # Create agents
            Teach_agent_1 = agents.agent_1_name()
            Teach_agent_2 = agents.agent_2_name()

            # Define tasks
            Teach_task_1 = tasks.task_1_name(
                Teach_agent_1,
                self.var1,
                self.var2,
                self.age,
                self.pdf,
                self.ch
            )

            Teach_task_2 = tasks.task_2_name(
                Teach_agent_2,
                [Teach_task_1]
                # save_and_execute
            )

            # Initialize Crew
            crew = Crew(
                agents=[Teach_agent_1, Teach_agent_2],
                tasks=[Teach_task_1, Teach_task_2],
                #process=Process.hierarchical,
                manager_llm=llm,
                verbose=True
            )

            # Execute Crew
            result = crew.kickoff()
            return result

        except Exception as e:
            print(f"An error occurred: {e}")
            return None



# Main execution
if __name__ == "__main__":
    print("## Welcome to Crew AI physics teacher ")
    print("-------------------------------")

    # Get user inputs with validation
    while True:
        try:
            ch = input("Tell me what is the chapter you need me to explain: ").strip()
            age = int(input("How old are you: "))
            if age <= 0:
                raise ValueError("Age must be a positive number")
            var1 = input("What do you want me to focus on: ").strip()
            var2 = input("Is there anything you want to tell me: ").strip()
            
            # Define the PDF path
            pdf_path = "C:/Users/NTC/Desktop/musa/statistical mechanics _1/Ch1.pdf"
            
            # Create and run the teaching crew
            Teach_crew = TeachCrew(ch, age, pdf_path, var1, var2)
            result = Teach_crew.run()
            
            if result:
                print("\n\n########################")
                print("## Here is your Teach crew run result:")
                print("########################\n")
                print(result)
            else:
                print("Failed to generate the result.")
            break
            
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

# import os
# import torch
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# from crewai import Crew
# from agents import teachAgents
# from tasks import techerTasks
# from tools.file_io import save_and_execute
# from textwrap import dedent
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)

# # Set your local model directory
# local_model_path = "C:/models/my_finetuned_model"  # Path to your downloaded model

# try:
#     # Load the model and tokenizer from your local path
#     model = AutoModelForSeq2SeqLM.from_pretrained(local_model_path)
#     tokenizer = AutoTokenizer.from_pretrained(local_model_path)
#     logging.info("Local model loaded successfully.")
# except Exception as e:
#     logging.error(f"Error loading the local model: {e}")
#     exit(1)  # Exit if model loading fails

# # Path to the PDF file (static or dynamic)
# pdf_path = "C:/Users/PC/Desktop/master_jo/statistical mechanics _1/Ch1.pdf"

# class TeachCrew:
#     def __init__(self, ch, age, pdf, var1, var2):
#         self.ch = ch
#         self.age = age
#         self.pdf = pdf
#         self.var1 = var1
#         self.var2 = var2

#     def run(self):
#         try:
#             # Initialize agents and tasks
#             agents = teachAgents()
#             tasks = techerTasks()

#             # Create agents
#             Teach_agent_1 = agents.agent_1_name()
#             Teach_agent_2 = agents.agent_2_name()

#             # Define tasks
#             Teach_task_1 = tasks.task_1_name(
#                 Teach_agent_1,
#                 self.var1,
#                 self.var2,
#                 self.age,
#                 self.pdf,
#                 self.ch
#             )

#             Teach_task_2 = tasks.task_2_name(
#                 Teach_agent_2,
#                 [Teach_task_1]
#             )

#             # Initialize Crew
#             crew = Crew(
#                 agents=[Teach_agent_1, Teach_agent_2],
#                 tasks=[Teach_task_1, Teach_task_2],
#                 manager_llm=model,  # Assign the fine-tuned model as the manager LLM
#                 verbose=True
#             )

#             # Execute Crew
#             result = crew.kickoff()
#             return result

#         except Exception as e:
#             logging.error(f"An error occurred: {e}")
#             return None

# # Main execution block
# if __name__ == "__main__":
#     print("## Welcome to Crew AI Physics Teacher ##")
#     print("----------------------------------------")

#     ch = input(dedent("Tell me which chapter you need me to explain: "))
#     age = input(dedent("How old are you? "))
#     pdf = pdf_path  # Use static PDF path (or input() for dynamic entry)
#     var1 = input(dedent("What do you want me to focus on? "))
#     var2 = input(dedent("Is there anything else you want to tell me? "))

#     Teach_crew = TeachCrew(ch, age, pdf, var1, var2)
#     result = Teach_crew.run()

#     if result:
#         print("\n########################")
#         print("## Teach Crew Run Result:")
#         print("########################\n")
#         print(result)
#     else:
#         print("Failed to generate the result.")

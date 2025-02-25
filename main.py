import os
from crewai import Crew, Process
from langchain_community.llms import OpenAI , Ollama
#from langchain.llms import Ollama 
# from langchain_community.llms import Ollama 
from crewai import LLM
from agents import teachAgents
from tasks import techerTasks
from tools.file_io import save_and_execute
from textwrap import dedent
import logging
import textwrap
# Load environment variables from .env file
# load_dotenv()
from dotenv import load_dotenv
# import os
from crewai import LLM
load_dotenv()
# OPENAI_API_KEY="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"

# from langchain_ollama import OllamaLLM

# Environment variables for static file handling (if needed)
static_directory = os.getenv('STATIC_DIRECTORY', 'static')
static_route = os.getenv('STATIC_ROUTE', '/static')
static_name = os.getenv('STATIC_NAME', 'static_files')
api_key = os.getenv('OPENAI_API_KEY')

# # Initialize the language model
# llm = Ollama(
#    model="deepseek-r1:1.5b ",
#    base_url="http://localhost:11434"
# )
OPENAI_API_KEY="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"
# # gpt-3.5-turbo

llm = LLM(
    model="openai/gpt-3.5-turbo-instruct-0914", # call model by provider/model_name
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)

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



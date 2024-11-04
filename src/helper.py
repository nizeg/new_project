import sys
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool  # Example: using a CrewAI tool


# Function to load environment variables
def load_env(env_file='/Users/nize/Documents/Coding/new_project/.env'):
    print("Inside load_env function")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Checking if {env_file} exists: {os.path.exists(env_file)}")

    # Print the absolute path of the .env file
    abs_path = os.path.abspath(env_file)
    print(f"Absolute path of .env file: {abs_path}")
    print(f"Checking if absolute path exists: {os.path.exists(abs_path)}")

    if os.path.exists(env_file):
        try:
            with open(env_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        try:
                            key, value = line.split('=', 1)
                            os.environ[key.strip()] = value.strip()
                        except ValueError:
                            print(f"Skipping malformed line: {line}")
            print("Environment variables loaded.")
        except Exception as e:
            print(f"Error loading environment file: {str(e)}")
    else:
        print(f"{env_file} file not found.")



# Function to initialize an agent with common properties
def initialize_agent(role, goal, backstory, tools=[], memory=True, verbose=False):
    """Initializes an Agent with standardized settings."""
    return Agent(
        role=role,
        goal=goal,
        memory=memory,
        verbose=verbose,
        backstory=backstory,
        tools=tools
    )

# Function to initialize a task with default settings
def initialize_task(description, expected_output, agent, tools=[], async_execution=True, output_file=None):
    """Initializes a Task with standardized settings."""
    return Task(
        description=description,
        expected_output=expected_output,
        tools=tools,
        agent=agent,
        async_execution=async_execution,
        output_file=output_file
    )

# Function to create a Crew with agents and tasks
def initialize_crew(agents, tasks, process=Process.sequential):
    """Initializes a Crew with specified agents, tasks, and process."""
    return Crew(
        agents=agents,
        tasks=tasks,
        process=process
    )

# Example function to kickoff a crew with inputs
def kickoff_crew(crew, inputs):
    """Kicks off the crew process with the provided inputs."""
    return crew.kickoff(inputs=inputs)

# Example setup of Serper tool with environment variables
def get_search_tool():
    """Returns an instance of the SerperDevTool initialized with an API key from environment."""
    api_key = os.getenv('SERPER_API_KEY')
    if not api_key:
        raise ValueError("SERPER_API_KEY is not set in the environment variables.")
    return SerperDevTool()

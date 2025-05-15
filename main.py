# taskgpt/main.py

from agent import TaskGPTAgent
import json

def main():
    agent = TaskGPTAgent()
    print("🔮 Welcome to TaskGPT")
    goal = input("Enter your goal: ")
    result = agent.plan(goal)
    print("\n📋 Task Plan:\n")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()

# taskgpt/agent.py

class TaskGPTAgent:
    def __init__(self):
        pass

    def plan(self, goal):
        steps = self._break_down(goal)
        prioritized = self._prioritize(steps)
        with_tools = self._suggest_tools(prioritized)
        return {
            "goal": goal,
            "steps": with_tools
        }

    def _break_down(self, goal):
        # Naive keyword-based step breakdown
        goal_lower = goal.lower()
        if "blog" in goal_lower:
            return ["Choose a blog theme", "Fork a template", "Customize content", "Deploy on GitHub Pages"]
        elif "resume" in goal_lower:
            return ["Pick a template", "Fill out personal info", "Convert to PDF", "Host it online"]
        else:
            return ["Research the goal", "List needed actions", "Assign priorities", "Execute steps"]

    def _prioritize(self, steps):
        return [{"step": s, "priority": i+1} for i, s in enumerate(steps)]

    def _suggest_tools(self, steps):
        tool_map = {
            "theme": "Jekyll Themes",
            "fork": "GitHub",
            "customize": "Markdown/Editor",
            "deploy": "GitHub Pages",
            "template": "Overleaf/Canva",
            "pdf": "PDF Exporter",
            "host": "Netlify/Vercel",
            "research": "Google",
            "execute": "Manual/Script"
        }
        for step in steps:
            step_lower = step["step"].lower()
            step["tool"] = next((tool for keyword, tool in tool_map.items() if keyword in step_lower), "N/A")
        return steps

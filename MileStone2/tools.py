from langchain.tools import Tool
import requests

# Tool 1: Calculator
def calculator(expression: str) -> str:
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception:
        return "Calculator error: Invalid expression."

calculator_tool = Tool(
    name="calculator",
    func=calculator,
    description="Use this tool to solve math expressions like '12 * 5 + 3'."
)

# Tool 2: Weather (API-based)
def get_weather(city: str) -> str:
    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url, timeout=10).json()
        temp = data["current_condition"][0]["temp_C"]
        return f"Current temperature in {city} is {temp}°C."
    except Exception:
        return "Weather error: Could not fetch weather data."

weather_tool = Tool(
    name="weather",
    func=get_weather,
    description="Use this tool to get current temperature of a city."
)

# Export tools list
tools = [calculator_tool, weather_tool]

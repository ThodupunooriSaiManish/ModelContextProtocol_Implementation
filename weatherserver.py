from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

@mcp.tool()
def get_current_weather(location: str) -> str:
    """
    Retrieves the live weather status for a given location or city.
    """
    return "Its raining in hyderabad"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
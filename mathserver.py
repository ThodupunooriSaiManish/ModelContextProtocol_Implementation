from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathServer")

@mcp.tool()
def addition(a: int, b: int) -> int:
    """
    Adds two numbers together. Use this tool when you need to calculate sums.
    """
    return a + b

@mcp.tool()
def multiplication(a: int, b: int) -> int:
    """
    Multiplies two numbers together. Use this tool when calculating products.
    """
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")
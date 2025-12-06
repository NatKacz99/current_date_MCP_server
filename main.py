from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Date Server")

@mcp.tool()
def get_current_date() -> str:
    """
    Returns the current date in YYYY-MM-DD format.
    An agent can use this tool to get today's date.
    """
    return datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    mcp.run()
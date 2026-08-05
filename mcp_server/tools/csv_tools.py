# tools/csv_tools.py

from server import mcp
from utils.file import oky_csv
@mcp.tool()
def summarize_csv_file(filename: str) -> str:

    return oky_csv(filename)
# tools/csv_tools.py

from server import mcp
from utils.file import oky_parqet
@mcp.tool()
def summarize_parqet_file(filename: str) -> str:

    return oky_parqet(filename)
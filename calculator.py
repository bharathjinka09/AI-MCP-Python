# server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("Calculator Server")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a subtraction tool
@mcp.tool() 
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

# Add a multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Add a division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Add a square tool
@mcp.tool()
def square(a: int) -> int:
    """Square a number"""
    return a * a

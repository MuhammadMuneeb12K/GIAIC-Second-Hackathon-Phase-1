#!/usr/bin/env python3
"""
Main entry point for the Todo Application - Phase I Implementation

A professional Python console application that provides basic todo list functionality
with in-memory storage. The application features a menu-driven CLI interface allowing
users to add, view, update, delete, and mark tasks as complete/incomplete.
"""

import sys
import os
# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.cli.menu import TaskCLI


def main():
    """Main function to run the Todo application."""
    cli = TaskCLI()
    cli.run()


if __name__ == "__main__":
    main()
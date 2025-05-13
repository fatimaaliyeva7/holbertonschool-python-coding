#!/usr/bin/python3
"""Define a class Square with a private attribute size."""

class Square:
    """Represents a square with a private size attribute."""
    
    def __init__(self, size):
        """Initialize the Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size


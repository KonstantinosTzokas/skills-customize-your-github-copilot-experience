"""
Python Text Processing Starter Code

This starter template provides a framework for text processing tasks.
Complete the implementation by adding functions for string manipulation,
file I/O, and text analysis.
"""

import os
from collections import Counter
from typing import List, Dict


# ============================================================================
# TASK 1: String Manipulation and Text Transformation
# ============================================================================

def convert_case(text: str, case_type: str) -> str:
    """
    Convert text to specified case type.
    
    Args:
        text: Input text string
        case_type: Type of case conversion ('upper', 'lower', 'title')
    
    Returns:
        Converted text string
    """
    # TODO: Implement case conversion logic
    pass


def count_word_occurrences(text: str, word: str) -> int:
    """
    Count occurrences of a word in text (case-insensitive).
    
    Args:
        text: Input text string
        word: Word to search for
    
    Returns:
        Number of occurrences
    """
    # TODO: Implement word counting logic
    pass


def find_and_replace(text: str, old_text: str, new_text: str) -> str:
    """
    Find and replace all occurrences of text.
    
    Args:
        text: Input text string
        old_text: Text to find
        new_text: Replacement text
    
    Returns:
        Text with replacements made
    """
    # TODO: Implement find and replace logic
    pass


# ============================================================================
# TASK 2: File I/O Operations
# ============================================================================

def read_file(file_path: str) -> str:
    """
    Read entire file content.
    
    Args:
        file_path: Path to the file
    
    Returns:
        File content as string
    
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    # TODO: Implement file reading with error handling
    pass


def read_file_lines(file_path: str) -> List[str]:
    """
    Read file and return lines as a list.
    
    Args:
        file_path: Path to the file
    
    Returns:
        List of lines (with newlines removed)
    
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    # TODO: Implement file reading line by line
    pass


def write_file(file_path: str, content: str, append: bool = False) -> None:
    """
    Write content to a file.
    
    Args:
        file_path: Path to the file
        content: Content to write
        append: If True, append to file; if False, overwrite
    """
    # TODO: Implement file writing with proper mode handling
    pass


# ============================================================================
# TASK 3: Text Analysis and Data Processing
# ============================================================================

def count_word_frequency(text: str) -> Dict[str, int]:
    """
    Count frequency of each word in text.
    
    Args:
        text: Input text string
    
    Returns:
        Dictionary with words as keys and counts as values
    """
    # TODO: Implement word frequency counting
    pass


def get_most_common_words(text: str, top_n: int = 10) -> List[tuple]:
    """
    Get the most common words in text.
    
    Args:
        text: Input text string
        top_n: Number of top words to return
    
    Returns:
        List of (word, count) tuples sorted by frequency
    """
    # TODO: Implement most common words extraction
    pass


def calculate_text_statistics(text: str) -> Dict[str, float]:
    """
    Calculate statistics about the text.
    
    Args:
        text: Input text string
    
    Returns:
        Dictionary with statistics:
        - 'word_count': Total number of words
        - 'unique_words': Number of unique words
        - 'avg_word_length': Average length of words
        - 'sentence_count': Approximate number of sentences
    """
    # TODO: Implement text statistics calculation
    pass


def filter_lines_by_keyword(text: str, keyword: str) -> List[str]:
    """
    Filter lines containing a specific keyword.
    
    Args:
        text: Input text string (multiline)
        keyword: Keyword to search for
    
    Returns:
        List of lines containing the keyword
    """
    # TODO: Implement keyword filtering
    pass


def remove_duplicates(text: str, separator: str = '\n') -> str:
    """
    Remove duplicate lines from text.
    
    Args:
        text: Input text string
        separator: Line separator character
    
    Returns:
        Text with duplicates removed
    """
    # TODO: Implement duplicate removal
    pass


# ============================================================================
# Main Program
# ============================================================================

if __name__ == "__main__":
    # Example usage - implement test cases here
    sample_text = """
    Python is a powerful programming language.
    Python is used for web development and data science.
    Data science is a growing field in technology.
    """
    
    # Test your implementations here
    print("Text Processing Assignment")
    print("=" * 50)
    
    # TODO: Add test cases for your implementations

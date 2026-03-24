"""
Python Data Structures Starter Code

This starter template provides a framework for working with lists, dictionaries,
sets, and tuples. Complete the implementation by adding functions to master
these fundamental data structures.
"""

from typing import List, Dict, Set, Tuple, Any, Union


# ============================================================================
# TASK 1: Working with Lists and Tuples
# ============================================================================

def list_operations(numbers: List[int]) -> Dict[str, Any]:
    """
    Perform various list operations and return results.
    
    Args:
        numbers: List of integers
    
    Returns:
        Dictionary with operation results:
        - 'sorted_asc': List sorted in ascending order
        - 'sorted_desc': List sorted in descending order
        - 'reversed': Reversed list
        - 'unique': List with duplicates removed
    """
    # TODO: Implement list operations
    pass


def filter_and_transform(numbers: List[int], threshold: int) -> List[int]:
    """
    Filter numbers greater than threshold and square them.
    
    Args:
        numbers: List of integers
        threshold: Minimum value (exclusive)
    
    Returns:
        List of squared numbers that exceed threshold
    """
    # TODO: Use list comprehension for efficient filtering and transformation
    pass


def tuple_packing_unpacking(a: int, b: str, c: float) -> Tuple[int, str, float]:
    """
    Pack multiple values into a tuple and return it.
    
    Args:
        a: An integer
        b: A string
        c: A float
    
    Returns:
        Tuple containing all three values
    """
    # TODO: Create and return tuple
    pass


def unpack_and_process(data: Tuple[int, int, int]) -> int:
    """
    Unpack tuple values and return their sum.
    
    Args:
        data: Tuple of three integers
    
    Returns:
        Sum of all tuple elements
    """
    # TODO: Unpack tuple and calculate sum
    pass


# ============================================================================
# TASK 2: Mastering Dictionaries
# ============================================================================

def create_student_record(name: str, age: int, grades: List[float]) -> Dict[str, Any]:
    """
    Create a student record dictionary with nested data.
    
    Args:
        name: Student name
        age: Student age
        grades: List of grade values
    
    Returns:
        Dictionary with student information
    """
    # TODO: Create dictionary with student data and nested structure
    pass


def count_word_frequency(words: List[str]) -> Dict[str, int]:
    """
    Count frequency of each word in the list.
    
    Args:
        words: List of words
    
    Returns:
        Dictionary mapping words to their frequencies
    """
    # TODO: Implement word frequency counting using dictionary
    pass


def group_by_category(items: List[Dict[str, Any]], category_key: str) -> Dict[str, List[Any]]:
    """
    Group items by a specific category.
    
    Args:
        items: List of dictionaries representing items
        category_key: Key to group by
    
    Returns:
        Dictionary where keys are categories and values are lists of items
    """
    # TODO: Group items by category
    pass


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries, with dict2 values overriding dict1.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary
    
    Returns:
        Merged dictionary
    """
    # TODO: Merge dictionaries
    pass


def get_nested_value(data: Dict[str, Any], key_path: List[str], default: Any = None) -> Any:
    """
    Retrieve value from nested dictionary using key path.
    
    Args:
        data: Nested dictionary
        key_path: List of keys representing path (e.g., ['user', 'address', 'city'])
        default: Value to return if key path doesn't exist
    
    Returns:
        Value at key path or default value
    """
    # TODO: Navigate nested dictionary and return value
    pass


# ============================================================================
# TASK 3: Sets and Advanced Operations
# ============================================================================

def find_common_elements(list1: List[int], list2: List[int]) -> List[int]:
    """
    Find elements that appear in both lists (intersection).
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        List of common elements (sorted)
    """
    # TODO: Use sets to find intersection
    pass


def find_unique_elements(list1: List[int], list2: List[int]) -> List[int]:
    """
    Find elements that appear in either list but not both (symmetric difference).
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        List of unique elements from both sets
    """
    # TODO: Use sets to find symmetric difference
    pass


def remove_duplicates(items: List[Any]) -> List[Any]:
    """
    Remove duplicates from list while preserving order.
    
    Args:
        items: List that may contain duplicates
    
    Returns:
        List with duplicates removed, order preserved
    """
    # TODO: Remove duplicates using sets while maintaining order
    pass


def find_unique_in_first_only(list1: List[str], list2: List[str]) -> List[str]:
    """
    Find elements that are in list1 but not in list2.
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        List of elements that are only in list1 (sorted)
    """
    # TODO: Use set difference operation
    pass


def set_operations_demo(set1: Set[int], set2: Set[int]) -> Dict[str, Set[int]]:
    """
    Perform and return results of all set operations.
    
    Args:
        set1: First set of integers
        set2: Second set of integers
    
    Returns:
        Dictionary with results:
        - 'union': Union of both sets
        - 'intersection': Common elements
        - 'difference': Elements in set1 but not set2
        - 'symmetric_diff': Elements in either set but not both
    """
    # TODO: Perform all set operations
    pass


# ============================================================================
# Main Program
# ============================================================================

if __name__ == "__main__":
    # Example data for testing
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    
    print("Data Structures in Python Assignment")
    print("=" * 50)
    
    # TODO: Add test cases for your implementations

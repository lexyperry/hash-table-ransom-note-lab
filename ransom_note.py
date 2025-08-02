def can_construct(ransomNote: str, magazine: str) -> bool:
    
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    letter_counts = {}

    for char in magazine:
        if char in letter_counts:
            letter_counts[char] += 1
        else: 
            letter_counts[char] = 1 
    
    for char in ransomNote:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
        letter_counts[char] -= 1

    return True
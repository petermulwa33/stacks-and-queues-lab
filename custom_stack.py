
def is_valid_parentheses(s: str) -> bool:
    """
    Return True if all parentheses and brackets are balanced.

    Uses a stack (LIFO) to match opening brackets
    with their corresponding closing brackets.
    """

    stack = []

    # Map closing brackets to their matching opening brackets.
    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:

        # Push opening brackets onto the stack.
        if char in '({[':
            stack.append(char)

        # Check closing brackets.
        elif char in ')}]':

            # No opening bracket exists to match this closing bracket.
            if not stack:
                return False

            # The most recent opening bracket must match.
            if stack.pop() != matching_brackets[char]:
                return False

    # All opening brackets must have been matched.
    return len(stack) == 0

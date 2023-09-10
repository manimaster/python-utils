def are_parentheses_balanced(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            # Pop the topmost element from stack, if it's empty assign a dummy value '#'
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped element matches the current character's mapping
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    # Return True if the stack is empty, False otherwise
    return not stack

if __name__ == "__main__":
    string_input = input("Enter a string: ")
    if are_parentheses_balanced(string_input):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")

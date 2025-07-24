def is_valid(s):
    stack = []
    map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in map.values():
            stack.append(char)
        elif char in map:
            if not stack or stack.pop() != map[char]:
                return False
    return not stack

print(is_valid("({[]})")) 

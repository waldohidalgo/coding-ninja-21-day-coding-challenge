def isValidParenthesis(s: str) -> bool:
    # Write your code here
    stack=[]
    for c in s:
        if c=='(' or c=='[' or c=='{':
            stack.append(c)
        elif c==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
        elif c==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                return False
        elif c=='}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                return False
    return not stack

s="[[}["
print(isValidParenthesis(s))
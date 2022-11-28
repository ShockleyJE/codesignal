def solution(inputString):
    chars = list(inputString)
    if len(chars) == 0: return ''
    stack = []
    for i,c in enumerate(chars):
        if c == '(':
            stack.append(i)
        elif c == ')':
            last_open=stack.pop()
            chars[last_open:i] = chars[i:last_open:-1]
    return ''.join(c for c in chars if c not in '()')
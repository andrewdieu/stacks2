def eval_rpn(s):
    tokens = s.split()

    stack = []

    for token in tokens:
        if token not in '+-/*':
            stack.append(int(token))
            continue
    
        if len(stack) < 2: return stack.pop()


        r_op = stack.pop()
        l_op = stack.pop()
        result = None

        if token == '+': result = l_op + r_op
        elif token == '-': result = l_op - r_op
        elif token == '*': result = l_op * r_op
        elif token == '/': result = int(l_op / r_op)

        stack.append(result)

    result = stack.pop()

    return result

def main():
    tests = [
        {'inputs': '3 2 +',         'results': 5},
        {'inputs': '2 1 + 3 *',     'results': 9},
        {'inputs': '4 13 5 / +',    'results': 6},
        {'inputs': '2',             'results': 2},
        {'inputs': '5 +',           'results': 5},
    ]

    for i in range(len(tests)):
        print(f'Test {i}:', eval_rpn(tests[i]['inputs']) == tests[i]['results'])

main()

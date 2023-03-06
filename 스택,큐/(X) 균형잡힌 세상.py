# https://www.acmicpc.net/problem/4949

while True:
    x= input()
    stack = []
    if x == '.':
        break
    for i in x:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif len(stack) == 0:
                print('no')
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif len(stack) == 0:
                print('no')
                break 
    if stack:
        print('no')
    else:
        print('yes')                    




        


                                                    

                    

                

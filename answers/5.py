from copy import deepcopy

def main():
    data = []
    with open('input 5.txt','r',encoding='utf-8') as f:
        for line in f:
            if '[' not in line:
                break
            data.append(line)

    stacks_2d = []
    for line in data:
        if '[' not in line:
            break
        line = '  ' + line.strip('\n')
        stack = []
        for j in range(len(line)):
            if (j+1)%4 == 0 and j != 0:
                stack.append(line[j])
        stacks_2d.append(stack)

    stacks = []
    for i in range(len(stacks_2d[0])):
        stack = []
        for j in range(len(stacks_2d)):
            if stacks_2d[j][i] == ' ':
                continue
            stack.append(stacks_2d[j][i])
        stacks.append(stack)

    [print(stack) for stack in stacks]

    stacks_2 = deepcopy(stacks)

    raw = open('input 5.txt','r',encoding='utf-8').readlines()
    for line in raw:
        line = line.strip()
        if 'move' not in line:
            continue

        line = line.replace('move','')
        line = line.replace('from','')
        line = line.replace('to','')
        line = [int(x) for x in list(filter(None, line.split(' ')))]
        stacks = move(line[0],line[1]-1,line[2]-1,stacks)
        stacks_2 = move_2(line[0],line[1]-1,line[2]-1,stacks_2)
    print(f'Part 1: {"".join([stack[0] for stack in stacks])}')
    print(f'Part 2: {"".join([stack_2[0] for stack_2 in stacks_2])}')

def move(n,old,new,stacks):
    [stacks[new].insert(0,stacks[old].pop(0)) for x in range(n)]
    return stacks

def move_2(n,old,new,stacks_2):
    to_move = [stacks_2[old].pop(0) for x in range(n)]
    [stacks_2[new].insert(0,to_move.pop()) for x in range(n)]
    return stacks_2

if __name__ == '__main__':
    main()

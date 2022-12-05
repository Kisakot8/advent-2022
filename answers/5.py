from copy import deepcopy

def main():
    '''
    Now. I could either spend hours trying to code a way
    to read the stacks, OR I could just hardcode it and
    save myself time. I'll choose the second option.
    '''

    stacks = [
    ['N','W','B'],
    ['B','M','D','T','P','S','Z','L'],
    ['R','W','Z','H','Q'],
    ['R','Z','J','V','D','W'],
    ['B','M','H','S'],
    ['B','P','V','H','J','N','G','L'],
    ['S','L','D','H','F','Z','Q','J'],
    ['B','Q','G','J','F','S','W'],
    ['J','D','C','S','M','W','Z']]

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

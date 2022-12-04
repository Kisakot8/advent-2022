def main():
    with open('input 4.txt','r',encoding='utf-8') as f:
        count1 = 0
        count2 = 0
        for line in f:
            pair = line.strip().split(',')
            pair = [pair[x].split('-') for x in range(2)]
            pair = [[int(y) for y in x] for x in pair]
            s1 = set(range(pair[0][0],pair[0][1]+1))
            s2 = set(range(pair[1][0],pair[1][1]+1))
            if s1.issubset(s2) or s2.issubset(s1):
                count1 += 1
            if len(s1 & s2) != 0:
                count2 += 1
        print(f'Part 1: {count1}')
        print(f'Part 2: {count2}')


if __name__ == '__main__':
    main()

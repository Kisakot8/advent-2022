import string

def main():
    with open('input 3.txt','r',encoding='utf-8') as f:
        repeated = []
        for line in f:
            line = line.strip()
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]
            for letter in second_half:
                if letter in first_half:
                    repeated.append(letter)
                    break
    letters = [[x,string.ascii_letters.index(x)+1] for x in string.ascii_letters]
    priorities = {k:v for (k,v) in letters}
    priorities_sum = 0
    for letter in repeated:
        priorities_sum += priorities[letter]
    
    print(priorities_sum) # Part 1 solution

    with open('testing text.txt','r',encoding='utf-8') as f:
        groups = []
        temp = []
        for i, line in enumerate(f, start=1):
            line = line.strip()
            temp.append(line)
            if i%3 == 0:
                groups.append(temp)
                temp = []
    badges = []
    for group in groups:
        badges.append(list(set(group[0]) & set(group[1]) & set(group[2]))[0])

    badges_priorities = [priorities[x] for x in badges]
    print(sum(badges_priorities)) # Part 2 solution

if __name__ == '__main__':
    main()

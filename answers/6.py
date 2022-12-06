def main():
    data = open('1 input.txt','r',encoding='utf-8').readline()

    for i in range(4,len(data)):
        marker = data[i-4:i]
        if len(list(marker)) == len(set(list(marker))):
            print(f'Part 1: {i}')
            break
    
    for i in range(14,len(data)):
        marker = data[i-14:i]
        if len(list(marker)) == len(set(list(marker))):
            print(f'Part 2: {i}')
            break

if __name__ == '__main__':
    main()

def main():
    nums = make_list('1 input.txt')
    largest_elf = find_largest(nums)
    print(largest_elf)
    top_3 = find_top_3(nums)
    print(top_3)

def find_top_3(lst:list[int]) -> int:
    sums = 0
    for i in range(3):
        x = find_largest(lst)
        print(x)
        sums += x[0]
        lst.pop(x[1])
    return sums

def find_largest(lst:list[int]) -> int:
    largest = [0,0]
    for i, sub_lst in enumerate(lst):
        if sum(sub_lst) > largest[0]:
            largest = [sum(sub_lst),i]
    return largest

def make_list(filename:str) -> list[int]:
    with open(filename,'r',encoding='utf-8') as file:
        lst = []
        temp = []
        lines = file.readlines()
        for line in lines:
            if line != '\n':
                temp.append(int(line.strip('\n')))
                if line == lines[-1]:
                    lst.append(temp)
            else:
                lst.append(temp)
                temp = []
    return lst

if __name__ == '__main__':
    main()

# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(len(data)//2, -1, -1):
        array_to_heap(data, i, swaps)
    return swaps

def array_to_heap(data, i, swaps):
    min = i

    l = 2 * i + 1
    if l < len(data) and data[l] < data[min]:
        min = l

    r = 2 * i + 2
    if r < len(data) and data[r] < data[min]:
        min = r

    if i != min:
        swaps.append([i, min])
        data[i], data[min] = data[min], data[i]
        array_to_heap(data, min, swaps)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    cmd = input()
    if "I" in cmd:
        n = int(input())
        data = list(map(int, input().split()))
    
    elif "F" in cmd:
        fn = input()
        if not "a" in fn:
            f = open("tests/" + fn, "r")
            text = f.read()
            f.close()
            n = int(text.partition("\n")[0])
            data = list(map(int, text.partition("\n")[2].split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

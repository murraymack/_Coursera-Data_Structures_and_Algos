# python3
def pair_wise_calc3(b):
    max_1, max_2 = 0, 0
    if len(b) == 1:
        return b[0]*1
    if len(b) == 2:
        return b[0] * b[1]
    for i in range(len(b)):
        if b[i] > max_1:
            max_2 = max_1
            max_1 = b[i]
    if max_2 == 0:
        for i in range(1, len(b)):
            if b[i] > max_2:
                max_2 = b[i]
    return max_1 * max_2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(pair_wise_calc3(input_numbers))
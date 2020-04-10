# python3
def pair_wise_calc1a(b):
    b.sort(reverse=True)
    return b[0] * b[1]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(pair_wise_calc1a(input_numbers))
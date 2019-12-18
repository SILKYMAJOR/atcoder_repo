
def main():
    n = int(input())
    h_list = list(map(int, input().split()))

    max_count = 0
    count = 0
    for i in range(n-1):
        if h_list[i] >= h_list[i+1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)

    print(max_count)


if __name__ == '__main__':
    main()


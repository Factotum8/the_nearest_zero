def calculate_distances(count: int, cells: list[int]):
    result_distances = [float('inf')] * count
    distance, last_zero_indx = None, None

    # def iterate_over(iterator):
    #     for i in iterator:
    #         if cells[i] == 0:
    #             distance = 0
    #             last_zero_indx = i
    #         result_distances[i] = min(result_distances[i], distance)
    #         distance += 1
    #     return last_zero_indx
    #
    # r = iterate_over(range(cells.index(0), count))
    # iterate_over(reversed(range(r)))

    for i in range(cells.index(0), count):
        if cells[i] == 0:
            distance = 0
            last_zero_indx = i
        result_distances[i] = min(result_distances[i], distance)
        distance += 1

    for i in reversed(range(last_zero_indx)):
        if cells[i] == 0:
            distance = 0
        result_distances[i] = min(result_distances[i], distance)
        distance += 1

    return result_distances


def main():
    try:
        cells_count = int(input())
        cells = [int(house) for house in input().split()]
    except ValueError as e:
        print(f"wrong input: {e}")
        return
    calculate_distances(cells_count, cells)


if __name__ == '__main__':
    main()

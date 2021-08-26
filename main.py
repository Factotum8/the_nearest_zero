def calculate_distances(count: int, cells: list[int]) -> list[int]:
    """
    * Заполняем пустой лист result_distances бесконечностями float('inf'). Длина листа как у "улицы".
    * С перового нуля проходим по "улице" в конец, вычисляя расстояния до участков. Записываем в лист result_distances
        min(текущая дистанция до нуля, result_distances[текущий индекс]).
    * С последнего нуля идём в начало "улицы" беря min(текущая дистанция до нуля, result_distances[текущий индекс]).
    """
    nearest_symbol = 0

    def iterate_over(iterator):
        distance, symbol_indx = None, None
        for i in iterator:
            if cells[i] == nearest_symbol:
                distance = 0
                symbol_indx = i
            result_distances[i] = min(result_distances[i], distance)
            distance += 1
        return symbol_indx

    result_distances = [float('inf')] * count
    last_symbol_index = iterate_over(range(cells.index(nearest_symbol), count))
    iterate_over(reversed(range(last_symbol_index + 1)))

    return result_distances


def main():
    try:
        cells_count = int(input())
        cells = [int(house) for house in input().split()]
    except ValueError as e:
        print(f"wrong input: {e}")
        return
    print(calculate_distances(cells_count, cells))


if __name__ == '__main__':
    main()

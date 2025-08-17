""" Задача 4. """
import os
import sys


def calculate_moves(arr):
    if not arr:
        return 0
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    median = sorted_arr[n // 2]  
    
    moves = sum(abs(num - median) for num in arr)
    
    if moves > 20:
        print("Невозможно привести массив к одному числу за 20 ходов")
        return None
    
    print(f"Минимальное количество ходов: {moves}")
    return moves

def main():
    
    data_file = sys.argv[1]

    with open(data_file, 'r') as file:
        arr = []
        for line in file:
            stripped = line.strip()
            arr.append(int(stripped))
        
        calculate_moves(arr)
   

if __name__ == "__main__":
    main()
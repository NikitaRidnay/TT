""" Задача 1. """

def calculate_arr_path(n, m):
    path = []
    current = 1
    
    while True:
        path.append(str(current)) 
        current = (current + m - 2) % n + 1
        if current == 1:
            break
    
    return ''.join(path)  

def main():
    print("Введите параметры для двух массивов (4 целых числа)")
    
    n1 = int(input("Размер первого массива (n1): "))
    m1 = int(input("Шаг для первого массива (m1): "))
    n2 = int(input("Размер второго массива (n2): "))
    m2 = int(input("Шаг для второго массива (m2): "))
    
    
    path1 = calculate_arr_path(n1, m1)
    path2 = calculate_arr_path(n2, m2)
    
    result = path1 + path2
    print("\nРезультат:")
    print(result)

if __name__ == "__main__":
    main()
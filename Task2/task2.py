""" Задача 2. """

import sys

def main():
    
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    with open(ellipse_file, 'r') as f:
            lines = f.readlines()
            center = tuple(map(float, lines[0].split()))
            radius = tuple(map(float, lines[1].split()))
        
    with open(points_file, 'r') as f:
        points = [tuple(map(float, line.split())) for line in f.readlines()]
        
    if len(points) < 1 or len(points) > 100:
        print("Ошибка: количество точек должно быть от 1 до 100")
        return
        
    results = []
    for point in points:
        x_diff = (point[0] - center[0]) / radius[0]
        y_diff = (point[1] - center[1]) / radius[1]
        value = x_diff**2 + y_diff**2
            
        if abs(value - 1.0) < 1e-10: 
            results.append("0")
        elif value < 1.0:
            results.append("1")
        else:
            results.append("2")
        
    print("\n".join(results))

        
    


if __name__ == "__main__":
    main()
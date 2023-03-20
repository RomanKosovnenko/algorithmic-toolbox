from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def minimum_distance_squared(points):
    def _minimum_distance_squared(points):
        if len(points) <= 3:
            return minimum_distance_squared_naive(points)

        mid = len(points) // 2
        left_points = points[:mid]
        right_points = points[mid:]

        left_min_distance_squared = _minimum_distance_squared(left_points)
        right_min_distance_squared = _minimum_distance_squared(right_points)

        min_distance_squared = min(left_min_distance_squared, right_min_distance_squared)

        strip_points = [point for point in points
                        if abs(point.x - points[mid].x) < sqrt(min_distance_squared)]

        strip_points.sort(key=lambda point: point.y)

        for i, point in enumerate(strip_points):
            for j in range(i + 1, len(strip_points)):
                if (strip_points[j].y - point.y) >= sqrt(min_distance_squared):
                    break
                min_distance_squared = min(min_distance_squared,
                                           distance_squared(point, strip_points[j]))

        return min_distance_squared

    points.sort(key=lambda point: point.x)
    return sqrt(_minimum_distance_squared(points))

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(minimum_distance_squared(input_points)))

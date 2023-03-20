from sys import stdin


def min_refills(distance, tank, stops):
    if tank > distance:
        return 0

    stops.append(distance)
    c_tank = tank
    c_pos = 0
    count = 0

    for i in range(len(stops)):
        next_distance = stops[i] - c_pos
        if next_distance > c_tank:
            if next_distance > tank:
                return -1
            count += 1
            c_pos = stops[i-1]
            c_tank = tank
        c_tank -= next_distance
        c_pos += next_distance

    # write your code here
    return count


if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))

"""
for number 123456, get 2 numbers that match the following
(123+456)^2 == 123456

ie: 328329
328 + 239 = 567
567 * 567 = 321489
321489 != 328329
False
"""
from math import sqrt


def split_numbers(num):
    combinations = []
    s = 0
    t = 0
    i = 0

    while i <= num:
        results = [t, s, i]
        v = results

        if t == num - 1 and s == num - 1:
            break
        i += 1
        if i == num:
            s += 1
            i = 0
        if s == num:
            s = 0
            t += 1

        if len(set(v)) != 3:
            continue
        combinations.append(v)

    return combinations


def get_two_numbers(number):
    results = []
    numbers = [x for x in str(number)]
    # print(numbers)
    base = sqrt(number)
    num1 = split_numbers(len(numbers))
    # print("NUMS 1", num1)
    num2 = split_numbers(len(numbers) + len(numbers) % 2)
    # print("NUMS 2", num2)
    for k in num1:
        # print("K:", k)
        for g in num2:
            # print("G:", g)
            if len(set(k).intersection(set(g))):
                continue
            number1 = int("".join([numbers[x] for x in k]))
            number2 = int("".join([numbers[x] for x in g]))

            if number1 + number2 != base:
                continue

            row = [number1, number2]
            row.sort()
            if row not in results:
                results.append(row)

    return results


if __name__ == "__main__":
    # print(573 * 573)

    n = 130321
    s = str(n)
    print(int(s[4] + s[3] + s[2]))
    print(int(s[0] + s[1] + s[5]))

    r = get_two_numbers(n)
    for k in r:
        print(k)

    print("LEN:", len(r))
    # numbers = split_numbers(6)
    # print(f"\n{len(numbers)}")

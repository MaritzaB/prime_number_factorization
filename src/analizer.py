from prime_number_fact import criba, number, euclides, euclidex, euclidex1
import time

first_number = 155181148463
second_number = 118764578488
numbers = (first_number, second_number)


def timer(function, numbers):
    init_time = time.time_ns()
    function(numbers[0], numbers[1])
    final_time = time.time_ns()
    total_time = final_time - init_time
    return total_time


print(timer(euclidex, numbers))
print(timer(euclidex1, numbers))
print(timer(euclides, numbers))

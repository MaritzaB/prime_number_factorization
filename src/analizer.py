from prime_number_fact import criba, number, euclides, euclidex, euclidex1
import time

first_number = 15518
second_number = 11876

def timer(function,first_number,second_number):
    init_time = time.time_ns()
    function(first_number,second_number)
    final_time = time.time_ns()
    total_time = final_time-init_time
    return total_time
    
print(timer(euclidex,first_number,second_number))
print(timer(euclidex1,first_number,second_number))

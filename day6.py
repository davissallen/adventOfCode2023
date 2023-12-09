def solve_part_two_but_runs_out_of_memory(memo, time_remaining, current_speed, distance_traveled, is_button_pressed):
    if time_remaining == 0:
        return distance_traveled
    if time_remaining < 0:
        return 0

    if is_button_pressed:
        # two choices: hold button, or let go of button
        return (
            # hold button
            solve_part_two_but_runs_out_of_memory(memo, time_remaining - 1, current_speed + 1, 0, True) +
            # let go
            solve_part_two_but_runs_out_of_memory(memo, time_remaining - 1, current_speed + 1, 0, False)
        )
    else:
        return solve_part_two_but_runs_out_of_memory(memo, time_remaining - 1, current_speed, distance_traveled + current_speed, False)


def solve_part_two_slow():
    """
    2
    x,1 = 1
    
    3
    x,1,1 = 2
    x,x,2 = 2
    
    4
    x,1,1,1 = 3
    x,x,2,2 = 4
    x,x,x,3 = 3
    
    5
    x,1,1,1,1 = 4
    x,x,2,2,2 = 6
    x,x,x,3,3 = 6
    x,x,x,x,4 = 4
    
    6
    x,1,1,1,1,1 = 5
    x,x,2,2,2,2 = 8
    x,x,x,3,3,3 = 9
    x,x,x,x,4,4 = 8
    x,x,x,x,x,5 = 5
    
    7
    x,1,1,1,1,1,1 = 6
    x,x,2,2,2,2,2 = 10
    x,x,x,3,3,3,3 = 12
    x,x,x,x,4,4,4 = 12
    x,x,x,x,x,5,5 = 10
    x,x,x,x,x,x,6 = 6
    
    8
    x,1,1,1,1,1,1,1 = 7
    x,x,2,2,2,2,2,2 = 12
    x,x,x,3,3,3,3,3 = 15
    x,x,x,x,4,4,4,4 = 16
    x,x,x,x,x,5,5,5 = 15
    x,x,x,x,x,x,6,6 = 12
    x,x,x,x,x,x,x,7 = 7
    
    9
    x,1,1,1,1,1,1,1,1 = 9 - 1 = 8
    x,x,2,2,2,2,2,2,2 = previous - 1 * 2/1 = 14
    x,x,x,3,3,3,3,3,3 = previous - 2 * 3/2 = ...
    x,x,x,x,4,4,4,4,4 = previous - 3 * 4/3 = ...
    x,x,x,x,x,5,5,5,5 = 
    x,x,x,x,x,x,6,6,6 = 
    x,x,x,x,x,x,x,7,7 = 
    x,x,x,x,x,x,x,x,8 = 

    
    ...
    it is kind of like fibbonacci, at least in the sense that the numbers for a particular row can be derived from
    those around it
    ...

           1
          2 2
         3 4 3
        4 6  6 4
      5  8  9  8 5
    6 10 12 12 10 6
    
    relationship: n = the sum of the two above it minus 
    """
    time_remaining = 44707080
    distance_record = 283113411341491

    memo = [1]
    for i in range(time_remaining - 2):
        if i % 4470708 == 0:
            print(time.ctime() + ' - ' + str(i / 4470708 * 10) + '% done')
        temp = [n + idx + 1 for idx, n in enumerate(memo)]
        temp.append(len(temp) + 1)
        memo = temp
    return sum(1 for n in memo if n > distance_record)


def solve_part_two_fast_enough():
    # just made vars here instead of parsing an input file
    time_remaining = 44707080
    distance_record = 283113411341491

    # note: in my test case, the time remaining is even (not odd, which matters here)
    count = 0
    num = time_remaining - 1
    for i in range(1, time_remaining // 2):
        num = int((num - i) / i * (i + 1))
        if num > distance_record:
            count += 1
    return count * 2 - 1


if __name__ == '__main__':
    answer = solve_part_two_fast_enough()
    print(answer)

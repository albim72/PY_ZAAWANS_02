def znajdz_sume_liczb_pierwszych(minimum,maximum):
    total = 0
    for number in range(minimum,maximum+1):
        count = 0
        for i in range(2,(number//2+1)):
            if number%i == 0:
                count+=1
                break
        if count == 0 and number != 1:
            total += number
    return total

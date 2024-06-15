numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
is_prime = True
for i in range(len(numbers)):
        for n in range(2,int(numbers[i]**0.5)+1):
            if numbers[i] % n == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print('Primes: ',primes)
print('Not_primes: ',not_primes)
def is_prime(n):return 0 not in [n%i for i in range(2,n//2+1)]
primes2 = [i for i in range(2,1000) if is_prime(i)]
print([ i for i in  [t for t in range(2,1000) if is_prime(t)] if sum([int(k) for k in str(i)]) % 2 == 1])


# primes = []
# for i in range(2,1000) :
#     for j in range(2,i): 
#         if i%j == 0 :break
#     else: primes.append(i) if sum([int(k) for k in str(i)]) % 2 == 1 else None
# print(primes)




# primes = []
# for i in range(2,1000):
#     for j in range(2,i):
#         if i%j== 0:
#             break
#     else:
#         if sum([int(k) for k in str(i)]) % 2 == 1:
#             primes.append(i)
# print(primes)







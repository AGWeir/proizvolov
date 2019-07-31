# A python proof for Proizvolov's identity
# Given a set of N integers split into 2 equal sets and sorted min-max, max-min
# Sum of differences always = (N/2)^2
# e.g N = 10 > 25
import itertools
import datetime

def prove_proizvolov(n):
    if n % 2 != 0:
        print("Proizvolov's identity only holds for even numbers")
    t0 = datetime.datetime.now()
    ints = [x for x in range(1,n + 1)]
    combs = itertools.combinations(ints, int(n/2))
    ncombs = 0
    for set1 in combs:
        set2 = [x for x in ints if x not in set1]
        set2.sort(reverse=True)  
        total = sum([abs(set2[x] - set1[x]) for x in range(int(n/2))])
        ncombs += 1
    if int((len(ints) / 2) ** 2) == total:
        print('When N =', n, 'proof is correct for', ncombs,'possible combinations')
    else:
        print('Not proven for N = ', n)
    print('Execution time:', datetime.datetime.now() - t0)
    
## e.g.
for n in range(2, 20,2):
    print(prove_proizvolov(n))

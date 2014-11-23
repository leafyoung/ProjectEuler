fun sumEvenFibs limit f0 f1 sum = 
    if f1 >= limit then sum
    else case (f1 mod 2 = 0) of (true) => sumEvenFibs limit f1 (f1+f0) (sum+f1)
                              | (false) => sumEvenFibs limit f1 (f1+f0) sum;

print (Int.toString(sumEvenFibs 4000000 0 1 0));
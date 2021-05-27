#Using a while loop, create a list called L that contains the numbers 0 to 10.
# (i.e.: Your while loop should initialize a counter variable to 0. On each iteration,
# the loop should append the current value of the counter variable
# to L and then increase the counter by 1.
# The while loop should stop once the counter variable is greater than 10.)


L  = list(range(0, 11))
accum=0
idx=0

while idx < len(L):
    accum = accum + L[idx]
    idx=idx+1

    print(idx)

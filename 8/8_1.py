# 8.1 Triple Step: 

# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

# recursive solution

def combs(n):
    if n == 0 or n == 1 or n == 2:
        return n
    if n == 3:
        return 4
    return combs(n-1) + combs(n-2) + combs(n-3)

# memoization/dynamic_programming solution

def helper(n, mem):
    if n == 0 or n == 1 or n == 2:
        return n
    if n == 3:
        return 4
    
    if mem[n] is None:
        mem[n] = combs(n-1) + combs(n-2) + combs(n-3)
    return mem[n]
    
def combs_dp(n):
    return helper(n, [None for i in range(n+1)])

# print(combs_dp(50))
# print(combs(50))

k += 1          # 4
i = n           # 2 
while i > 0:    # 3 * (n + 1) 
   i -= 1       # 4 * n
# k += 1 <-> k = k + 1
# sum = 7n + 9

i = n             # 2
while i > 1:      # 3 * (log2(n) + 1)
   k += 1         # 4 * log2(n)
   i //= 2        # 4 * log2(n)
# sum = 11log2(n) + 5


i = 0               # 2
while i < n:        # 3 * (n + 1)
   j = 0            # 2 * n
   while j < i * i: # 5 * (n + m)
      k += 1        # 4 * m
      j += 1        # 4 * m
      i += 1        # 4 * m
# sum = 14n + 13m + 5

i = 1            # 2
while i < n:     # 3 * (m + 1)
   j = 1         # 3 * m
   while j < n:  # 3 * m * (m + 1)
      k += 1     # 4 * m^2
      j *= 2     # 4 * m^2
      i *= 2     # 4 * m

# m = log2(n)
# sum = 11m^2 + 12m + 5
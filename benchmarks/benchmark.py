"""
Benchmark Framework

Simple benchmarking utilities for pqcrypto-lab.
"""

import time

def benchmark(function, *args):

```
start = time.perf_counter()

result = function(*args)

end = time.perf_counter()

print(f"{function.__name__}: {(end-start):.6f} seconds")

return result
```

if **name** == "**main**":

```
print("Benchmark framework initialized.")
```

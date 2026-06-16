import numpy as np

# fruits = {
#     "mango":  [9, 6],
#     "banana": [8, 4],
#     "lemon":  [2, 3.67],
# }

# new_fuits = [2,4]

# fruits["mango"]
# distance = np.sqrt()
# print(distance)
# distance = np.sqrt((new_fuits[0]-fruits["lemon"][0])**2 + (new_fuits[1]-fruits["lemon"][1])**2)
# print(distance)

# for key, value in fruits.items():
#     distance = np.sqrt((new_fuits[0]-value[0])**2 + (new_fuits[1]-value[1])**2)
#     print(key, round(distance,2)) # round(distance)

import random,time

N_DOCS = 50000
DIM = 384

vector_list = []
for _ in range(N_DOCS):
    vector = []
    for _ in range(DIM):
        vector.append(random.random())
    vector_list.append(vector)
    
docs = vector_list

query=[]
for _ in range(DIM):
    query.append(random.random())

start_time = time.time()
distances = []
for doc in docs:
    distance = 0
    for i in range(DIM):
        distance += (doc[i] - query[i])**2
    distances.append(np.sqrt(distance))
end_time = time.time()
print("Execution time:", end_time - start_time)


docs_np = np.array(docs, dtype=np.float16)
query_np = np.array(query, dtype=np.float16)

start_time = time.time()
distances = np.sqrt(np.sum((docs_np - query_np)**2, axis=1))
end_time = time.time()
print("Execution time for numpy approach:", end_time - start_time)


### Why so fast?
# 1. **Python loops are interpreted** — every `x*y` does type-checking + object overhead
# 2. **NumPy runs compiled C loops** over raw memory
# 4. **`@` calls BLAS** — decades-optimized linear algebra libraries

# > 🧠 **Mental model for today:** *"A `for` loop over data in an AI pipeline is probably wrong."*











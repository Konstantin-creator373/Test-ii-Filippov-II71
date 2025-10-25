import random

generation_key = random.randint(2, 5)
def generation():
    for i in range(generation_key):
        print(random.randint(0,1), random.randint(0,1), random.randint(0,1))

generation()


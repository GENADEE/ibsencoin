import proof_of_work
for i in range(1,100):
    print("...")
    rand_str = str(i)
    proof_of_work.pow(rand_str,2)
    pass
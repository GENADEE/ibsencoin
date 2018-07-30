import proof_of_work
for i in range(1,10):
    print("...")
    rand_str = str(i)
    proof_of_work.pow(rand_str,8)
    pass

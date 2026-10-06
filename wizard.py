def wizard(N,start,duels):
    owner = start
    changed_hand = 1
    for i in range(N):
        owner = [0][0]
        changed_hand = 1
    print(owner)
wizard(3, "A", ("BA", "CB", "DA"))
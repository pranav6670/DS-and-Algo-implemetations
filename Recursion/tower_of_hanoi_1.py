def move(origin, destination):
    print(F"Move the disk from {origin} to {destination}.")


def hanoi(num_disks, f, v, t):
    if num_disks == 0:
        pass
    else:
        hanoi(num_disks-1, f, t, v)  # Move n-1 disks from A to B using C.
        move(f, t)  # Move a disk from A to C.
        hanoi(num_disks-1, v, f, t)  # move n-1 disks from B to C using A.


hanoi(3, 'A', 'B', 'C')

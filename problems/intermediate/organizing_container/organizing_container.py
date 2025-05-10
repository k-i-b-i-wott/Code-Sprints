def organizingContainers(container):
    n = len(container)
    
    # Calculate total balls in each container (row sums)
    container_sums = [sum(row) for row in container]
    
    # Calculate total balls of each type (column sums)
    type_sums = [0] * n
    for i in range(n):
        for j in range(n):
            type_sums[j] += container[i][j]
    
    # Sort both lists to compare
    container_sums.sort()
    type_sums.sort()
    
    # If the sorted lists are equal, it's possible to organize
    return "Possible" if container_sums == type_sums else "Impossible"

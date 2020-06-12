# read the input
# input is on the form: i d1 d2 .. dn
# where i is the number of iterations and n is the number of pairs

# inp = input().split()
inp = '6 1#101 10#00 011#11'.split()

# k = number of iterations
k = int(inp[0])

# we initialize the list of dominos/pairs
dominos = []

# the list of dominos is filled with user input
for i in range(1, len(inp)):
    domino = inp[i].split("#")
    dominos.append(domino)

print("Running pcp with input: " + str(dominos))

# n = number of dominos
n = int(len(dominos))


def pcp():
    # (1) create a solutions list
    print("Number of dominos: " + str(n))
    solutions = []
    for i in range(0, n):
        print(dominos[i])
        xi = dominos[i][0]
        yi = dominos[i][1]
        if (xi == yi):
            return dominos[i]
        if (len(xi) < len(yi)):
            if (yi[:len(xi)] == xi):
                solutions.append(dominos[i])
        if (len(yi) < len(xi)):
            if (xi[:len(yi)] == yi):
                solutions.append(dominos[i])

    print("Solutions after (1): " + str(solutions))

    print("Number of iterations: " + str(k))
    # (2) loop through each iteration k
    for i in range(k):
        new_solutions = []
        for solution in solutions:
            for j in range(0, n):
                new_solution = [solution]
                xj = dominos[j][0]
                yj = dominos[j][1]
                new_solution.append([xj, yj])
                print(new_solution)
                xlist = ""
                ylist = ""
                for domino in new_solution:
                    xlist = xlist + domino[0]
                    ylist = ylist + domino[1]
                if(len(xlist) == len(ylist)):
                    new_solutions = new_solutions + new_solution
                if (len(xlist) < len(ylist)):
                    if (ylist[:len(xlist)] == xlist):
                        new_solutions = new_solutions + new_solution
                if (len(ylist) < len(xlist)):
                    if (xlist[:len(ylist)] == ylist):
                        new_solutions = new_solutions + new_solution
        print("New solutions: " + str(new_solutions))
        if (new_solutions == []):
            return []
        xlength = 0
        ylength = 0
        for solution in new_solutions:
            print("Solution: " + str(solution))
            xlength = xlength + len(solution[0])
            ylength = ylength + len(solution[1])
            print("xlength: " + str(xlength) + " ylength: " + str(ylength))
            if (xlength == ylength):
                return solution
        solutions = new_solutions
    return solutions

print("Solution to this pcp: " + str(pcp()))

# example input: 6 1#101 10#00 011#11
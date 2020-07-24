import os
os.system('cls' if os.name == 'nt' else 'clear')

# read the input
# input is on the form: i d1 d2 .. dn
# where i is the number of iterations and n is the number of pairs

# example inputs
# 6 1#101 10#00 011#11
# 70 001#0 01#011 01#101 10#001

print("Please specify the number of iterations you want to make and list the dominos to be used.")
print("Top and bottom rows of each domino are divided by a #.")
print("Example: 6 1#101 10#00 011#11")
inp = input("Input: ").split()

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# k = number of iterations
k = int(inp[0])

# we initialize the list of dominos/pairs
dominos = []

# the list of dominos is filled with user input
for i in range(1, len(inp)):
    domino = inp[i].split("#")
    dominos.append(domino)

print("Running pcp with input dominos: " + str(dominos))
print("")

# n = number of dominos
n = int(len(dominos))


def pcp():
    # (1) create a solutions list
    solutions = []
    for i in range(0, n):
        print(f"Domino {i}: {dominos[i]}")
        xi = dominos[i][0]
        yi = dominos[i][1]
        if (xi == yi):
            return dominos[i]
        if (len(xi) < len(yi)):
            if (yi[:len(xi)] == xi):
                solutions.append([dominos[i]])
        if (len(yi) < len(xi)):
            if (xi[:len(yi)] == yi):
                solutions.append([dominos[i]])

    # (2) loop through each iteration k
    for i in range(k):
        new_solutions = []
        for solution in solutions:
            for j in range(0, n):
                new_solution = solution.copy()
                xj = dominos[j][0]
                yj = dominos[j][1]
                new_solution.append([xj, yj])
                xlist = ""
                ylist = ""
                for domino in new_solution:
                    xlist += domino[0]
                    ylist += domino[1]
                if(len(xlist) == len(ylist)):
                    if (xlist == ylist):
                        new_solutions += [new_solution]
                if (len(xlist) < len(ylist)):
                    if (ylist[:len(xlist)] == xlist):
                        new_solutions += [new_solution]
                if (len(ylist) < len(xlist)):
                    if (xlist[:len(ylist)] == ylist):
                        new_solutions += [new_solution]
        if (new_solutions == []):
            return []
        xlength = 0
        ylength = 0
        for solution in new_solutions:
            xlength = 0
            ylength = 0
            for domino in solution:
                xlength += len(domino[0])
                ylength += len(domino[1])
            if (xlength == ylength):
                return solution
        solutions = new_solutions.copy()
    return []

res = pcp()

print("")
print("--------------------------------------------------------------------------------------")

if (res != []):
    print("Solution to this pcp: " + str(res))
    xlist = ""
    ylist = ""
    indexes = []
    for domino in res:
        xlist += domino[0]
        ylist += domino[1]
        indexes.append(dominos.index(domino))
    print(f"{xlist} <--- top row")
    print(f"{ylist} <--- bottom row")
    print(f"The following dominos were used (indexes): {str(indexes)}")
else:
    print("Could not find a solution for this pcp. Try with more iterations...")

print("--------------------------------------------------------------------------------------")
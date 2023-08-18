from gurobipy import *

eg1 = Model("eg1")

# index sets
N = range(2)  # variable num
M = range(3)  # constraint num

# parameters
c = [700, 900]
A = [[3, 5],
     [1, 2],
     [50, 20]]
b = [3600, 1600, 48000]

# variables
x = []
for i in N:
    x.append(eg1.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = "x"+str(i)))

# objective function
eg1.setObjective(
    quicksum(c[i] * x[i] for i in N),
    GRB.MAXIMIZE)

# constraints
eg1.addConstrs(
    (quicksum(A[j][i] * x[i] for i in N) <= b[j] for j in M),
    "wood, labor, machine")

#solve
eg1.optimize()

for var in x:
    print(var.varName, "=", var.x)
print("z =", eg1.objVal)
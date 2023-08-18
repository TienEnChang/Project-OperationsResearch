from gurobipy import *

# func
def solution(model):
    for var in eg.getVars():
        print(var.varName, "=", var.x)
    print("z =", eg.objVal)
    return

# index sets
I = range(2)  # variable num
J = range(2)  # constraint num

# parameters
c = [8, 5]
A = [[1, 1],
     [9, 5]]
b = [6, 45]

# instance
eg = Model("eg")

# variables
x = []         # aliasing
for i in I:
    x.append(eg.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = "x"+str(i+1)))

# objective function
eg.setObjective(
    quicksum(c[i] * x[i] for i in I),
    GRB.MAXIMIZE)

# constraints
eg.addConstrs(quicksum(A[j][i] * x[i] for i in I) <= b[j] for j in J)

while True:
    text = input("Add Constraints? ")
    if text == "n":
        break
    else:
        constr_info = text.split(" ")
        index = int(constr_info[0][1])-1
        val = int(constr_info[2])
        if constr_info[1] == "<=":
            eg.addConstr(x[index] <= val)
        elif constr_info[1] == ">=":
            eg.addConstr(x[index] >= val)

# solve
eg.optimize()
solution(eg)

# branch & bound

# x^1 = (3.75, 2.25),  z^1 = 41.25
   # x^2 = (3.88, 2),     z^2 = 41.11
      # x^4 = (3, 2),        z^4 = 34            {worse1}
         # x^5 = (4, 1.8),      z^5 = 41
            # x^6 = (4.44, 1),     z^6 = 40.55
               # x^8 = (4, 1),        z^8 = 37   {worse2}
               # x^9 = (5, 0),        z^9 = 40   {@2, optimal}
            # x^7 = (4, 2)         z^7           {infeasible}
   # x^3 = (3, 3),        z^3 = 39               {@1}
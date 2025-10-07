from ortools.linear_solver import pywraplp

def p4():
    solver = pywraplp.Solver.CreateSolver("SAT")
    #vars
    L = [4,5,3,2,4,3,5,4]
    B = [1,0,1,0,1,0,0,1]
    H = [0,1,0,1,0,1,0,1]
    s1 = [solver.IntVar(0,1,"s1"+str(i+1)) for i in range(8)]
    s2 = [solver.IntVar(0,1,"s2"+str(i+1)) for i in range(8)]
    #constraints
    for i in range(8):
        solver.Add(s1[i]+s2[i] == 1)
    solver.Add(solver.Sum(L[i]*s1[i] for i in range(8)) <= 16) # minute duration restrictions
    solver.Add(solver.Sum(L[i]*s1[i] for i in range(8)) >= 14)
    solver.Add(solver.Sum(L[i]*s2[i] for i in range(8)) <= 16)
    solver.Add(solver.Sum(L[i]*s2[i] for i in range(8)) >= 14)
    solver.Add(solver.Sum(B[i]*s1[i] for i in range(8)) == 2) # 2 ballads per side
    solver.Add(solver.Sum(B[i]*s2[i] for i in range(8)) == 2)
    solver.Add(solver.Sum(H[i]*s1[i] for i in range(8)) >= 3) # 3 hits minimum on side 1
    solver.Add(s1[4] + s1[5]>= 1) # song 5 or 6 on side 1
    solver.Add(s1[1] + s1[3] - s2[4] <= 1) # if song 2 and 4 on side 1, song 5 on side 2
    #objective function
    solver.Maximize(0)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Solutions Side 1: ", [s1[i].solution_value() for i in range(8)])
        print("Optimal Solutions Side 2: ", [s2[i].solution_value() for i in range(8)])
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p4()
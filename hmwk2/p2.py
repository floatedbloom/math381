from ortools.linear_solver import pywraplp

def p2():
    solver = pywraplp.Solver.CreateSolver("SAT")
    #vars
    g = [solver.IntVar(0,1,"g"+str(i)) for i in range(8)]
    #constraints
    solver.Add(g[0]+g[1]+g[5]>=1)
    solver.Add(g[1]+g[0]+g[2]+g[3]>=1)
    solver.Add(g[2]+g[1]+g[5]+g[3]+g[6]>=1)
    solver.Add(g[3]+g[1]+g[2]+g[4]>=1)
    solver.Add(g[4]+g[3]+g[6]+g[7]>=1)
    solver.Add(g[5]+g[0]+g[6]+g[2]>=1)
    solver.Add(g[6]+g[5]+g[2]+g[4]+g[7]>=1)
    solver.Add(g[7]+g[6]+g[4]>=1)
    #objective function
    solver.Minimize(solver.Sum(g[i] for i in range(8)))
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Optimal Value: {solver.Objective().Value()}")
        print(f"Optimal Solution: ", [g[i].solution_value() for i in range(8)])
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p2()
from ortools.linear_solver import pywraplp

def p2():
    solver = pywraplp.Solver.CreateSolver("SAT")
    #vars
    s1 = [solver.IntVar(0,1,"s1"+str(i+1)) for i in range(8)]
    s2 = [solver.IntVar(0,1,"s2"+str(i+1)) for i in range(8)]
    #constraints
    
    #objective function
    
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Optimal Value: {solver.Objective().Value()}")
        print(f"Optimal Solution: ")
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p2()
from ortools.linear_solver import pywraplp

def p1():
    solver = pywraplp.Solver.CreateSolver("SAT")
    #vars
    x = [solver.IntVar(0,1,"x"+str(i)) for i in range(14)]
    #constraints
    #titles
    solver.Add(x[6]+x[7]+x[8]>=1)
    solver.Add(x[0]+x[1]+x[4]>=1)
    #overlapping
    solver.Add(x[0]+x[3]<=1)
    solver.Add(x[1]+x[4]+x[6]<=1)
    solver.Add(x[7]+x[13]<=1)
    solver.Add(x[2]+x[9]+x[10]<=1)
    solver.Add(x[5]+x[8]+x[12]<=1)
    #sequences
    solver.Add(x[1]-x[0]<=0)
    solver.Add(x[3]-x[2]<=0)
    solver.Add(x[7]-x[6]<=0)
    #lunch
    solver.Add(x[13]+x[11]+x[7]<=1)
    #objective function
    solver.Maximize(solver.Sum(x[i] for i in range(14)))
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Optimal Value: {solver.Objective().Value()}")
        for i in range(14):
            print(f"Optimal Solution: {x[i].solution_value()}")
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p1()
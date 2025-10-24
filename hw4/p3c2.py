from ortools.linear_solver import pywraplp

def p3():
    #P2's solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #va1
    y_rr = solver.NumVar(0, 1, "y_rr")
    y_pp = solver.NumVar(0, 1, "y_pp")
    y_ss = solver.NumVar(0, 1, "y_ss")
    z = solver.NumVar(-solver.infinity(), solver.infinity(), "z")
    #constraints
    solver.Add(z >= -y_pp + y_ss)
    solver.Add(z >= y_rr - y_ss)
    solver.Add(z >= -y_rr + y_pp)
    solver.Add(y_rr + y_pp + y_ss == 1)
    #objective function
    solver.Minimize(z)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", round(solver.Objective().Value(),3))
        print("y_pp: ", round(y_pp.solution_value(),3))
        print("y_rr: ", round(y_rr.solution_value(),3))
        print("y_ss: ", round(y_ss.solution_value(),3))
    else:
        print("No optimal solution")


if __name__ == '__main__':
    p3()
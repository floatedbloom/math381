from ortools.linear_solver import pywraplp

def p3():
    #P2's solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #va1
    y_rs = solver.NumVar(0, 1, "y_rs")
    y_rp = solver.NumVar(0, 1, "y_rp")
    y_ps = solver.NumVar(0, 1, "y_ps")
    z = solver.NumVar(-solver.infinity(), solver.infinity(), "z")
    #constraints
    solver.Add(z >= -(1/3) * y_rp + (1/3) * y_ps)
    solver.Add(z >= (1/3) * y_rs - (1/3) * y_ps)
    solver.Add(z >= -(1/3) * y_rs + (1/3) * y_rp)
    solver.Add(y_rs + y_rp + y_ps == 1)
    #objective function
    solver.Minimize(z)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", round(solver.Objective().Value(),3))
        print("y_rp: ", round(y_rp.solution_value(),3))
        print("y_rs: ", round(y_rs.solution_value(),3))
        print("y_ps: ", round(y_ps.solution_value(),3))
    else:
        print("No optimal solution")


if __name__ == '__main__':
    p3()
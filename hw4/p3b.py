from ortools.linear_solver import pywraplp

def p3():
    #P1's solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #va1
    x_rs = solver.NumVar(0, 1, "x_rs")
    x_rp = solver.NumVar(0, 1, "x_rp")
    x_ps = solver.NumVar(0, 1, "x_ps")
    z = solver.NumVar(-solver.infinity(), solver.infinity(), "z")
    #constraints
    solver.Add(z <= (1/3) * x_rp - (1/3) * x_ps)
    solver.Add(z <= -(1/3) * x_rs + (1/3) * x_ps)
    solver.Add(z <= (1/3) * x_rs - (1/3) * x_rp)
    solver.Add(x_rs + x_rp + x_ps == 1)
    #objective function
    solver.Maximize(z)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", round(solver.Objective().Value(),3))
        print("x_rp: ", round(x_rp.solution_value(),3))
        print("x_rs: ", round(x_rs.solution_value(),3))
        print("x_ps: ", round(x_ps.solution_value(),3))
    else:
        print("No optimal solution")


if __name__ == '__main__':
    p3()
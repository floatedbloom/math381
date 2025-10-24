from ortools.linear_solver import pywraplp

def p3c():
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #here, each variable dictates the proportion of times that the choice denoted by its subscript is kept from the opponent's hands 
    #vars
    y_r = solver.NumVar(0, 1, "y_r")
    z = solver.NumVar(-solver.infinity(), solver.infinity(), "z")
    #constraints
    solver.Add(z >= 2*y_r-1)
    solver.Add(z >= -y_r)
    #objective function
    solver.Minimize(z)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", round(solver.Objective().Value(), 3))
        print("y_r: ", round(y_r.solution_value(), 3))
        print("x_s: ", round(1- y_r.solution_value(), 3))
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p3c()
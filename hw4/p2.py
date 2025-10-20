from ortools.linear_solver import pywraplp

def p1():
    #first, solving for player 1
    solver1 = pywraplp.Solver.CreateSolver('GLOP')
    #vars
    x1 = solver1.NumVar(0,solver1.infinity(), "x1")
    x2 = solver1.NumVar(0,solver1.infinity(), "x2")
    x3 = solver1.NumVar(0,solver1.infinity(), "x3")
    z = solver1.NumVar(-solver1.infinity(), solver1.infinity(), "z")
    #constraints
    solver1.Add(z <= 0.5*x1-x2-x3)
    solver1.Add(z <= -x1+0.5*x2-x3)
    solver1.Add(z <= -x1-x2+x3)
    solver1.Add(x1+x2+x3==1)
    solver1.Add(0 <= x1 <= 1)
    solver1.Add(0 <= x2 <= 1)
    solver1.Add(0 <= x3 <= 1)
    #objective function
    solver1.Maximize(z)
    #solve
    status = solver1.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", solver1.Objective().Value())
        print("x1", x1.solution_value())
        print("x2: ", x2.solution_value())
        print("x3: ", x3.solution_value())
    else:
        print("No optimal solution")

    #solving for player 2
    solver2 = pywraplp.Solver.CreateSolver('GLOP')
    #vars
    y1 = solver2.NumVar(0,solver2.infinity(), "y1")
    y2 = solver2.NumVar(0,solver2.infinity(), "y2")
    y3 = solver2.NumVar(0,solver2.infinity(), "y3")
    z2 = solver2.NumVar(-solver2.infinity(), solver2.infinity(), "z")
    #constraints
    solver2.Add(z >= 0.5*y1-y2-y3)
    solver2.Add(z >= -y1+0.5*y2-y3)
    solver2.Add(z >= -y1-y2+y3)
    solver2.Add(y1+y2+y3==1)
    solver2.Add(0 <= y1 <= 1)
    solver2.Add(0 <= y2 <= 1)
    solver2.Add(0 <= y3 <= 1)
    #objective function
    solver2.Minimize(z)
    #solve
    status = solver2.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", solver2.Objective().Value())
        print("y1: ", y1.solution_value())
        print("y2: ", y2.solution_value())
        print("y3: ", y3.solution_value())
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p1()
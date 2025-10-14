from ortools.linear_solver import pywraplp

def p1():
    solver = pywraplp.Solver.CreateSolver('GLOP')
    #vars
    x12 = solver.NumVar(0,solver.infinity(), "x12")
    x13 = solver.NumVar(0,solver.infinity(), "x13")
    x24 = solver.NumVar(0,solver.infinity(), "x24")
    x25 = solver.NumVar(0,solver.infinity(), "x25")
    x34 = solver.NumVar(0,solver.infinity(), "x34")
    x35 = solver.NumVar(0,solver.infinity(), "x35")
    x46 = solver.NumVar(0,solver.infinity(), "x46")
    x56 = solver.NumVar(0,solver.infinity(), "x56")
    #constraints
    solver.Add(0 <= x12 <= 500)
    solver.Add(0 <= x13 <= 400)
    solver.Add(0 <= x24 <= 300)
    solver.Add(0 <= x25 <= 250)
    solver.Add(0 <= x34 <= 200)
    solver.Add(0 <= x35 <= 150)
    solver.Add(0 <= x46 <= 400)
    solver.Add(0 <= x56 <= 350)
    solver.Add(x12 == x24+x25)
    solver.Add(x13 == x34+x35)
    solver.Add(x46 == x24+x34)
    solver.Add(x56 == x25+x35)
    #objective function
    solver.Maximize(x46+x56)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", solver.Objective().Value())
        print("x12: ", round(x12.solution_value(),2))
        print("x13: ", round(x13.solution_value(),2))
        print("x24: ", round(x24.solution_value(),2))
        print("x25: ", round(x25.solution_value(),2))
        print("x34: ", round(x34.solution_value(),2))
        print("x35: ", round(x35.solution_value(),2))
        print("x46: ", round(x46.solution_value(),2))
        print("x56: ", round(x56.solution_value(),2))
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p1()
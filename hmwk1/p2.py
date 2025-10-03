from ortools.linear_solver import pywraplp

def p2():
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #vars
    w1 = solver.NumVar(0, solver.infinity(), "w1")
    a1 = solver.NumVar(0, solver.infinity(), "a1")
    w2 = solver.NumVar(0, solver.infinity(), "w2")
    a2 = solver.NumVar(0, solver.infinity(), "a2")
    #constraints
    solver.Add(w1+w2 <= 1000)
    solver.Add(a1+a2 <= 800)
    solver.Add(0.2*w1 - 0.8*a1 >= 0)
    solver.Add(0.4*a2 - 0.6*w2 >= 0)
    #objective func
    solver.Maximize(1.5*(w1+a1)+1.3*(w2+a2)-0.5*(w1+w2)-0.4*(a1+a2))
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print(f"Objective value = {solver.Objective().Value()}")
        print(f"w1 = {w1.solution_value()}")
        print(f"a1 = {a1.solution_value()}")
        print(f"w2 = {w2.solution_value()}")
        print(f"a2 = {a2.solution_value()}")
    else:
        print("No optimal solution")

if __name__ == "__main__":
    p2()
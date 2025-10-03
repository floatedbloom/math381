from ortools.linear_solver import pywraplp

def p4():
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #vars
    f1 = solver.NumVar(0, solver.infinity(), "f1")
    f2 = solver.NumVar(0, solver.infinity(), "f2")
    p1 = solver.NumVar(0, solver.infinity(), "p1")
    p2 = solver.NumVar(0, solver.infinity(), "p2")
    p3 = solver.NumVar(0, solver.infinity(), "p3")
    p4 = solver.NumVar(0, solver.infinity(), "p4")
    p5 = solver.NumVar(0, solver.infinity(), "p5")
    p6 = solver.NumVar(0, solver.infinity(), "p6")
    #constraints
    solver.Add(f1+f2+p1 >= 4)
    solver.Add(f1+f2+p1+p2 >= 3)
    solver.Add(f1+f2+p1+p2+p3 >= 4)
    solver.Add(f2+p2+p3+p4 >= 6)
    solver.Add(f1+p3+p4+p5 >= 5)
    solver.Add(f1+f2+p4+p5+p6 >= 6)
    solver.Add(f1+f2+p5+p6 >= 8)
    solver.Add(f1+f2+p6 >= 8)
    solver.Add(p1+p2+p3+p4+p5+p6 <= 5)
    #objective func
    solver.Minimize(64*(f1+f2)+15*(p1+p2+p3+p4+p5+p6))
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print(f"Objective value = {solver.Objective().Value():0.2f}")
        print(f"f1 = {f1.solution_value():0.2f}")
        print(f"f2 = {f2.solution_value():0.2f}")
        print(f"p1 = {p1.solution_value():0.2f}")
        print(f"p2 = {p2.solution_value():0.2f}")
        print(f"p3 = {p3.solution_value():0.2f}")
        print(f"p4 = {p4.solution_value():0.2f}")
        print(f"p5 = {p5.solution_value():0.2f}")
        print(f"p6 = {p6.solution_value():0.2f}")
    else:
        print("No optimal solution")

if __name__ == "__main__":
    p4()
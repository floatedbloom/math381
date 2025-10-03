from ortools.linear_solver import pywraplp

def p3():
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #vars
    w11 = solver.NumVar(0, solver.infinity(), "w11")
    w12 = solver.NumVar(0, solver.infinity(), "w12")
    a11 = solver.NumVar(0, solver.infinity(), "a11")
    a12 = solver.NumVar(0, solver.infinity(), "a12")
    w21 = solver.NumVar(0, solver.infinity(), "w21")
    w22 = solver.NumVar(0, solver.infinity(), "w22")
    a21 = solver.NumVar(0, solver.infinity(), "a21")
    a22 = solver.NumVar(0, solver.infinity(), "a22")
    #constraints
    solver.Add(w11+a11 <= 300)
    solver.Add(w21+a21 <= 300)
    solver.Add(w11+w12+w21+w22 <= 1000)
    solver.Add(a11+a12+a21+a22 <= 800)
    solver.Add(0.2*w11+0.2*w12 - 0.8*a11 - 0.8*a12 >= 0)
    solver.Add(0.4*a21 +0.4*a22- 0.6*w21 - 0.6*w22 >= 0)
    #objective func
    solver.Maximize(1.5*(w11+a11)+1.25*(w12+a12)+1.3*(w21+a21)+(w22+a22)-0.5*(w11+w12+w21+w22)-0.4*(a11+a12+a21+a22))
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print(f"Objective value = {solver.Objective().Value():0.2f}")
        print(f"w11 = {w11.solution_value():0.2f}")
        print(f"w12 = {w12.solution_value():0.2f}")
        print(f"w21 = {w21.solution_value():0.2f}")
        print(f"w22 = {w22.solution_value():0.2f}")
        print(f"a11 = {a11.solution_value():0.2f}")
        print(f"a12 = {a12.solution_value():0.2f}")
        print(f"a21 = {a21.solution_value():0.2f}")
        print(f"a22 = {a22.solution_value():0.2f}")
    else:
        print("No optimal solution")

if __name__ == "__main__":
    p3()
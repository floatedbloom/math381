from ortools.linear_solver import pywraplp

def p3():
    solver = pywraplp.Solver.CreateSolver("SAT")
    #vars
    STUDENTS = [43,29,42,21,56,18,71]
    s = [solver.IntVar(0,1,"s"+str(i)) for i in range(7)]
    r = [None]*11
    r[0] = solver.IntVar(0,1,"AB")
    r[1] = solver.IntVar(0,1,"AC")
    r[2] = solver.IntVar(0,1,"BC")
    r[3] = solver.IntVar(0,1,"BD")
    r[4] = solver.IntVar(0,1,"BE")
    r[5] = solver.IntVar(0,1,"CD")
    r[6] = solver.IntVar(0,1,"DE")
    r[7] = solver.IntVar(0,1,"DF")
    r[8] = solver.IntVar(0,1,"DG")
    r[9] = solver.IntVar(0,1,"EF")
    r[10] = solver.IntVar(0,1,"FG")
    #constraints
    solver.Add(sum(r)==2)
    solver.Add(s[0] <= r[0]+r[1])
    solver.Add(s[1] <= r[0]+r[2]+r[3]+r[4])
    solver.Add(s[2] <= r[1]+r[2]+r[5])
    solver.Add(s[3] <= r[3]+r[5]+r[6]+r[7]+r[8])
    solver.Add(s[4] <= r[4]+r[6]+r[9])
    solver.Add(s[5] <= r[7]+r[9]+r[10])
    solver.Add(s[6] <= r[8]+r[10])
    #objective function
    solver.Maximize(solver.Sum(STUDENTS[i]*s[i] for i in range(len(s))))
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Optimal Value: {solver.Objective().Value()}")
        print(f"Optimal Solution: ", [r[i].solution_value() for i in range(len(r))])
    else:
        print("No optimal solution")

if __name__ == '__main__':
    p3()
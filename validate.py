def init_validate(plan):
    column_len = len(plan)
    row_len = len(plan[0])
    # making sure all rows are equal length and everything in the rows is a 1 or a 0
    if all(len(rows) == row_len and all(items in ['0','1','5','6','7'] for items in rows) for rows in plan):
        return [column_len, row_len]
    else:
        return []


#searches txt to find "entrance" represented by the number 5
def find_entrance(plan, column_len, row_len):
    
    for i in range(0, column_len):
        for j in range(0,row_len):
            if plan[i][j].wall == 5:
                return plan[i][j]
    
    return None

#searches txt to find "exit" represented by the number 7
def find_exit(plan, column_len, row_len):

    for i in range(1, column_len):
        for j in range(0,row_len):
            if plan[i][j].wall == 7:
                return plan[i][j]

    return None

#searches txt to find "fire" represented by the number 6
def find_fire(plan, column_len, row_len):
    
    for i in range(0, column_len - 1):
        for j in range(0, row_len -1):
            if plan[i][j].wall == 6:
                return plan[i][j]
    
    return None
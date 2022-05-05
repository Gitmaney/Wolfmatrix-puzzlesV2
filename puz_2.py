
def checknums(num, con, right_num, right_pos):
    count_right_num = 0
    count_right_pos = 0
    checknum = str(num).zfill(len(con))
    for i in range(len(con)):
        if checknum[i] in con:
            count_right_num +=1
        if checknum[i] == con[i]:
            count_right_pos += 1
    if right_num == count_right_num and correct_pos == count_right_pos:
        return true
        
def numbers(con1:str, con2:str, con3:str, con4:str, con5:str):
    #con1 -> one digit is right and in its place
    #con2 -> one digit is right but in the wrong place
    #con3 -> two digits are right but both are in the wrong place
    #con4 -> all digits are wrong
    #con5 -> one digit is right but in the wrong place
    start = 0
    for num in range(1000):
        if checknums(num,con1, 1, 1) and checknums(num,con2, 1, 0) and checknum(num,con3, 2, 0) and checknum(num,con4, 0, 0) and checknum(num,con5, 1, 0):
            print('The required number for padlock is {str(num).zfill(len(con1))}')
            break

numbers("682", "614", "206", "738", "380")
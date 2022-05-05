def checknums(num, con, right_number, right_pos):
    count_right_number = 0
    count_right_pos = 0
    checknum = str(num).zfill(len(con))
    for i in range(len(con)):
        if checknum[i] in con:
            count_right_num +=1
        if checknum[i] == con[i]:
            count_right_pos += 1
    if right_num == count_right_num and right_pos == count_right_pos:
        return true
        
def solution(con1:str, con2:str, con3:str, con4:str, con5:str):
    #con1 -> one digit right but in wrong place
    #con2 -> one digit right and in right place
    #con3 -> two digits correct but in wrong place
    #con4 -> all digits are wrong place
    #con5 -> one digit right but in wrong place
    start = 0
    for number in range(1000):
        if checknums(num,con1, 1, 0) and checknums(num,con2, 1, 1) and checknums(num,con3, 2, 0) and checknums(num,con4, 0, 0) and checknums(num,con5, 1, 0):
            print('The required solution is {num}')
            break

solution("147", "189", "964", "523", "286")
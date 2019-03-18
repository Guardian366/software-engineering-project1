def addNewUser(position, id):
    with open('database.txt', 'a+') as db_file:
        db_file.write(str(position) + ',' + str(id)+"\n")

def getUserId(position):
    with open('database.txt', 'r') as db_file:
        for aline in db_file:
            l_position, id = aline.split(',')
            if str(position) == l_position:
                return id

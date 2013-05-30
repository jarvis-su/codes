
def getTicketsList(fileName):
    list = []
    file = open(fileName,'r')
    try:
        lines = file.readlines()
        for l in lines:
            s = l.replace('\n','')
            list+=[s]
    finally:
        file.close()
    return list


def old_macdonald(name):
    result = ""
    for i in range(len(name)):
        if i == 0 or i == 3:
            result = result + name[i].upper()
        else :
            result = result + name[i].lower()
    return result





print(old_macdonald('macdonald'))   

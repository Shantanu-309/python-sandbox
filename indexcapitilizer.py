def myfunc(n):
    result = ''
    for i in range(len(n)):
        if i % 2 == 0:
            result = result + n[i].upper()
        else:
            result = result + n[i].lower()
    return result

print(myfunc('Anthropomorphism'))

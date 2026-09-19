def animal_crackers(text):
    for i in range(len(text)):
        if text[i] == " ":
            if text[0] == text[i + 1]:
                return True
            else:
                return False

    
    
print(animal_crackers('Levelheaded Llama'))
animal_crackers('Crazy Kangaroo')

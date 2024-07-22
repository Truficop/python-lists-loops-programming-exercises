def lyrics_generator(list):
    ritm = ''
    conteo_de_unos = 0
    for i in list:
        if i == 0:
            ritm += 'Boom '
            conteo_de_unos += 0
        elif i == 1:
            ritm += 'Drop the bass '
            conteo_de_unos += 1
            if conteo_de_unos == 3:
                ritm += '!!!Break the bass!!! '
    return ritm

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))

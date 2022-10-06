if __name__ == '__main__':
    names = ['Ala', 'Ela', 'Ola', 'Iwona', 'Ilona', 'Adam', 'Robert', 'Malgorzata', 'Dagmara']
    names_lengths = {}
    for name in names:
        if names_lengths.get(len(name)) is None:
            names_lengths[len(name)] = []
        names_lengths[len(name)].append(name)
    print(names_lengths)
    # genders = {'male': [], 'female': []}
    '''for gender in names:
        if gender[-1] == 'a':
            genders['female'].append(gender)
        else:
            genders['male'].append(gender)
    print(genders)'''

    """colors = ['red', 'green', 'red', 'blue', 'green', 'red', 'orange', 'yellow', 'orange']
    counted_colors = {}
    for color in colors:
        if counted_colors.get(color) is not None:
            counted_colors[color] += 1
        else:
            counted_colors[color] = 1
    print(set(colors))
    print(counted_colors)"""

'''if __name__ == '__main__':
    my_dict = { }
    my_dict['drzewo'] = 'lisciaste'
    my_dict['drzewo'] = 'iglaste'
    print(my_dict)
    del(my_dict['drzewo'])
    print(my_dict['drzewo'])
    print(my_dict.get('drzewo'))'''
# Writing

characters = ["Mario", "Lugi", "Peach", "Yoshi", "Bowser", "Toad"]

def write_characters_to_file(filename):
    # Open file
    file = open(filename, 'w+') # w+ can write() and read()
    # write to file
    for c in characters:
        char = f"{c}\n"
        file.write(char)

    file.seek(0, 0) # reset pointer : w+

    content = file.read()
    print(content)
    # close file
    file.close()

    return

def main():
    write_characters_to_file('../character.txt')
    return


if __name__ == '__main__':
    main()
# Appending

more_charactors = ['Diddy Kong', 'Donkey Kong', 'Wario']

def append_characters_to_file(filename):
    with open(filename, "a+") as f:
        f.seek(0)   # Move pointer to the beginning
        content = f.read()

        if content:
            f.write("\n\t# newAppend\n")   # Add blank line

        # Appending
        for c in more_charactors:
            f.write(c + '\n')

        f.seek(0)

        content = f.read()
        print(content)

def main():
    append_characters_to_file('../character.txt')

if __name__ == "__main__":
    main()
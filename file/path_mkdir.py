from pathlib import Path
# Path

current_file = 'characters.txt'

def create_path():

        current_dir_path = Path(__file__).parent.parent
        path_characters_dir = current_dir_path / 'characters'
        print(path_characters_dir)

        # path to make directory
        path_characters_dir.mkdir(parents=True, exist_ok=True)

        # path of file
        path_of_file = path_characters_dir / 'zelda.txt'

        with open(path_of_file, 'a+') as f:
             f.write('\nLink again')

             f.seek(0)
             
        #  Read    
        with open(path_of_file, 'r') as f:
             content = f.read()
             print(content)
             



def main():
    create_path()


if __name__ == '__main__':
    main()
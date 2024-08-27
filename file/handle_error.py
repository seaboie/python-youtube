from pathlib import Path

def open_file():
    current_dir_path = Path(__file__).parent.parent
    new_file_path = current_dir_path / 'does' / 'not' / 'exist.txt'

    try:
        with open(new_file_path, 'r') as f:
            content = f.read()
            print(content)

    except FileNotFoundError as e:
        print(f"{new_file_path} ::: doesn't exists \n {e}")
    except Exception as e:
        print(f"Exception as error::: \n {e}")


def main():
    open_file()   
    
    
if __name__ == "__main__":
    main()

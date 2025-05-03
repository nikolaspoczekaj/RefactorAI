
def check_last_line(file_path: str) -> bool:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            last_line = None
            for line in file:
                line = line.strip()
                if line:
                    last_line = line

            if last_line is None:
                return False

            return 'refactored by RefactorAI' in last_line
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return False


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)
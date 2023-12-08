def read_input(file_path):
    lines = []
    with open(file_path, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            lines.append(line.strip())
    return lines

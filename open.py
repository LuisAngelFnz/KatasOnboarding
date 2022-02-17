def main():
    file_path = 'mars.jpg'
    try:
        open(file_path, 'r')
    except IOError as err:

        if err.errno == 2:
            print(f'Archivo no encontrado: {file_path}')

        elif err.errno == 13:
            print(f'Imposible leer el archivo: {file_path}')
        else:
            raise err


if __name__ == '__main__':
    main()
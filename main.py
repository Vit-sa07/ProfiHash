import hashlib


def hash_file(path):
    # Создаем объект хэш-функции SHA3-256
    hasher = hashlib.sha3_256()

    # Открываем файл в бинарном режиме
    with open(path, 'rb') as file:
        # Читаем файл порциями по 8192 байт
        buff = file.read(8192)
        while buff:
            hasher.update(buff)
            buff = file.read(8192)

    # Возвращаем хэш-значение в шестнадцатеричном формате
    return hasher.hexdigest()


def save_file(hash_val, output_path):
    # Сохраняем хэш-значение в указанный файл
    with open(output_path, 'w') as file:
        file.write(hash_val)


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output_hash.txt"

    # Выполняем хэширование и сохраняем результат
    hash_val = hash_file(input_file)
    save_file(hash_val, output_file)

    print(f"Хэш сохранён в файл {output_file}: {hash_val}")

import time

real_password = "148889848522"

def brute_force(password):
    characters = "0123456789"
    max_length = len(password)

    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt_password = ''.join(attempt)
            print(f"Пробуем: {attempt_password}")

            if attempt_password == password:
                print(f"Пароль найден: {attempt_password}")
                return attempt_password


if __name__ == "__main__":
    import itertools

    start_time = time.time()
    found_password = brute_force(real_password)
    end_time = time.time()

    print(f"Найденный пароль: {found_password}")
    print(f"Время подбора: {end_time - start_time:.2f} секунд")
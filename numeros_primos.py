def is_primo (numero: int) -> bool:
    for i in range(2,numero):
        if numero % i == 0:
            # print(f"{numero} mod {i} ==",str(numero%i))
            return False
    return True


def run():
    print(is_primo(13))
    print(is_primo(45))


if __name__ == "__main__":
    run()

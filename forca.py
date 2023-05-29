import itertools

def des_senha(senha_test, caratere, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(caratere, repeat=length):
            password = ''.join(attempt)
            if password == senha_test:
                return password
    return None


senha_test = "aaa12"
# Conjunto de caracteres a serem usados na tentativa
caratere = "abcdefghijklmnopqrstuvwxyz0123456789"
# tamanho max da senha
max_length = 10

password_found = des_senha(senha_test, caratere, max_length)
if password_found:
    print("Senha: " + password_found)
else:
    print("Senha não encontrada.")

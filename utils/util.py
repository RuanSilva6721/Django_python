import unicodedata

def validaCpf(cpf: str) -> bool:
    return True if cpf.isdigit() and len(cpf) == 11 else False

def validaEmail(email: str) -> bool:
    return True if '@' in email and email.split('@')[1] else False

def nomeProprio(nome: str) -> str: 
    nome = list(map(lambda x: x.capitalize() if len(x) > 3 else x, nome.split(' ')))
    return ' '.join(nome)

def desacentua(texto: str) -> str:
    process = unicodedata.normalize("NFD", texto)
    process = process.encode("ascii", "ignore")
    process = process.decode("utf-8")
    return process

def abreviaNome(nome: str) -> str:
    nome = nome.split(' ')
    if len(nome) > 1:
        if len(nome[-2]) > 3:
            nome[-2] = nome[-2][0].upper() + '.'
    return ' '.join(nome)

if __name__ == '__main__':
    print(abreviaNome('ricardo dos santos'))
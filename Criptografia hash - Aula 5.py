import hashlib
#Importa o serviço hash.

#Coloque a senha ou valor que deseja criptografar.
SenhaFornecida = "Senha123"

def criar_hash(Senha):
   #Gera um código de 256 bits // mas pode ser reduzido.
    hash_obj = hashlib.sha256()
    
   #Converte a string em bytes.
    hash_obj.update(Senha.encode('utf-8'))
    
    #hexadecimal
    return hash_obj.hexdigest()

hash_resultado = criar_hash(SenhaFornecida)

print(f"A senha em formato hash é: {hash_resultado}")

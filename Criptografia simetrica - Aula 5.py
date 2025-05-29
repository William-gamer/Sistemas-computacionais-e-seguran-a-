from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Função para criptografar dados com DES
def criptografar_dados(chave, Mensagem):
    cipher = DES.new(chave, DES.MODE_CBC)  # Usando o modo CBC
    dados_padded = pad(Mensagem.encode(), DES.block_size)  # Preenchendo os dados para múltiplos de 8 bytes
    iv = cipher.iv
    dados_criptografados = cipher.encrypt(dados_padded)
    return iv + dados_criptografados  # Retorna o IV concatenado com os dados criptografados

def descriptografar_dados(chave, dados_criptografados):
    iv = dados_criptografados[:DES.block_size]  # O IV está nos primeiros 16 bytes
    dados_criptografados = dados_criptografados[DES.block_size:]  # O resto são os dados criptografados
    cipher = DES.new(chave, DES.MODE_CBC, iv)  
    dados_descriptografados = unpad(cipher.decrypt(dados_criptografados), DES.block_size)  # Removendo o padding
    return dados_descriptografados.decode()

#Chave
chave = get_random_bytes(8)  
#Coloque a mensagem que quer ser criptografada
Mensagem = "Senha"

#Criptografita
dados_criptografados = criptografar_dados(chave, Mensagem)
print(f"Mensagem criptografada: {dados_criptografados.hex()}")

#Descriptografita
dados_descriptografados = descriptografar_dados(chave, dados_criptografados)
print(f"Mensagem descriptografada: {dados_descriptografados}")

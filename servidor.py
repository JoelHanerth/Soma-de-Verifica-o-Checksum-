#!/usr/bin/env python3
import socket
import struct

def compute_checksum(data: bytes) -> int:
    """
    Calcula a soma de verificação (checksum) para um dado pacote de dados.
    Algoritmo:
      1. Se o tamanho dos dados for ímpar, adiciona um byte nulo para completar 16 bits.
      2. Divide os dados em palavras de 16 bits e soma-as utilizando a adição com complemento de 1.
      3. Retorna o complemento de 1 da soma final (os bits invertidos).
    """
    # Se o número de bytes for ímpar, adicione um byte zero
    if len(data) % 2:
        data += b'\0'
    s = 0
    # Percorre os dados de 2 em 2 bytes
    for i in range(0, len(data), 2):
        # Une dois bytes em um inteiro de 16 bits (big-endian)
        w = data[i] << 8 | data[i+1]
        s += w
        # Se houver overflow, adiciona o "carry"
        s = (s & 0xffff) + (s >> 16)
    # Retorna o complemento de 1 da soma
    return ~s & 0xffff

def main():
    host = ''         # Escuta em todas as interfaces
    port = 8080       # Porta definida para conexão

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Servidor ouvindo na porta {port}...")
        conn, addr = s.accept()
        with conn:
            print("Conexão estabelecida com:", addr)
            # Recebe o pacote completo (checksum + dados)
            packet = conn.recv(4096)
            if not packet:
                print("Nenhum pacote recebido.")
                return
            # Extrai os primeiros 2 bytes que contém o checksum enviado
            transmitted_checksum = struct.unpack("!H", packet[0:2])[0]
            data = packet[2:]
            try:
                print("Dados recebidos:", data.decode())
            except UnicodeDecodeError:
                print("Dados recebidos (binário):", data)
            # Calcula o checksum dos dados
            computed_checksum = compute_checksum(data)
            print(f"Soma de verificação transmitida: {hex(transmitted_checksum)}")
            print(f"Soma de verificação calculada:  {hex(computed_checksum)}")
            
            # Compara os checksums e define a resposta
            if transmitted_checksum == computed_checksum:
                response = "Checksum VÁLIDO"
            else:
                response = "Checksum INVÁLIDO"
            conn.sendall(response.encode())
            print("Resposta enviada ao cliente.")

if __name__ == '__main__':
    main()

# Soma-de-Verifica-o-Checksum-

Especificação do Trabalho Computacional: Soma de Verificação (Checksum)
com Python
Objetivo:
Desenvolver uma aplicação cliente-servidor em Python que implemente a soma de verificação
(checksum) para verificar a integridade dos dados enviados entre o cliente e o servidor.
Descrição do Trabalho:
O trabalho consiste em criar dois programas em Python: um para o cliente e outro para o servidor,
onde ambos devem implementar o cálculo e verificação de uma soma de verificação (checksum). O
cliente enviará dados para o servidor, e o servidor deve calcular a soma de verificação dos dados
recebidos e verificar se o valor está correto.
Requisitos:
1. Servidor:
• Deve ser implementado um servidor que escute uma porta de rede, aguardando
receber dados.
• Ao receber os dados, o servidor deve calcular a soma de verificação do pacote
recebido.
• O servidor deve responder com um valor indicando se a soma de verificação está
correta ou não.
2. Cliente:
• O cliente deve enviar um pacote de dados para o servidor.
• O cliente deve calcular a soma de verificação do pacote de dados antes de enviá-lo.
• Após o envio, o cliente deve aguardar a resposta do servidor e exibir se a soma de
verificação foi confirmada como correta ou se houve erro.
3. Cálculo da Soma de Verificação (Checksum):
• O cálculo da soma de verificação será realizado utilizando a adição em
complemento de 1 de todas as palavras de 16 bits no pacote de dados.
• O cliente e o servidor devem utilizar o mesmo algoritmo para calcular a soma de
verificação.
4. Protocolos de Comunicação:
• O cliente e o servidor devem se comunicar usando TCP/IP, para garantir uma troca
confiável de dados.
Funcionalidade Detalhada:
1. Servidor:
• Escuta a porta especificada (por exemplo, 8080).
• Quando um cliente se conecta, o servidor recebe os dados.
• Calcula a soma de verificação dos dados recebidos.
• Verifica se a soma de verificação recebida do cliente coincide com a calculada.
• Retorna uma mensagem ao cliente indicando se o checksum está correto.
2. Cliente:
• Solicita ao usuário que insira uma mensagem (pode ser uma string ou dados
binários).
• Calcula a soma de verificação do pacote de dados.
• Envia os dados e a soma de verificação para o servidor.
• Aguarda a resposta do servidor e exibe se o checksum é válido ou inválido.
Algoritmo de Cálculo da Soma de Verificação (Checksum):
1. Divida os dados em palavras de 16 bits.
2. Some todas as palavras utilizando o método de complemento de 1.
3. Inverta o resultado da soma de verificação (complemento de 1).
4. Transmita os dados junto com a soma de verificação.
5. O servidor verifica se a soma de verificação é válida ao calcular a soma e compará-la com a
enviada.
Anexo:
Extração de Dados UDP
Uma vez que você tenha capturado os pacotes UDP, você precisa extrair os dados da carga útil
(payload) dos pacotes. Os pacotes UDP são compostos por:
1. Cabeçalho UDP:
• Porta de origem e destino (16 bits cada)
• Tamanho do pacote UDP (16 bits)
• Soma de verificação (checksum) (16 bits)
2. Carga útil (Payload):
• São os dados que estão sendo transmitidos no pacote UDP.
A soma de verificação é calculada sobre a carga útil (payload), mas no caso de um pacote UDP, o
cabeçalho do protocolo também é incluído no cálculo.
Exemplo de extração dos dados:
Se você capturou pacotes UDP usando Wireshark ou tcpdump, a carga útil (payload) pode ser vista
diretamente. Caso contrário, ao capturar com tcpdump usando a opção -X, você verá os dados em
formato hexadecimal e ASCII.
Passo 3: Calcular a Soma de Verificação (Checksum)
O cálculo da soma de verificação no protocolo UDP é realizado com a adição em complemento de
1. A soma de verificação é calculada sobre a carga útil dos dados, bem como o cabeçalho do pacote
UDP, mas sem a soma de verificação que foi transmitida.
Passos para calcular o checksum:
1. Divida os dados em palavras de 16 bits: Cada palavra de 16 bits será somada ao total.
2. Realize a soma de todas as palavras de 16 bits: Faça a soma de todas as palavras de 16
bits, e caso ocorra um overflow (a soma ultrapassar 16 bits), o excesso (carregamento) é
adicionado de volta à soma.
3. Complemento de 1: Após a soma, o complemento de 1 do resultado final é calculado, ou
seja, todos os bits de 0 são transformados em 1 e os bits de 1 se tornam 0.
Para empacotar dados em UDP (User Datagram Protocol) e enviá-los através de uma rede, você
precisa seguir algumas etapas principais:
1. Criar o pacote de dados que você deseja enviar.
2. Configurar a comunicação UDP usando a biblioteca de socket em Python.
3. Enviar os dados via UDP para um destino, especificando o endereço IP e a porta do
servidor (ou receptor).
O UDP é um protocolo simples e sem conexão, ou seja, ele não garante a entrega dos pacotes, mas
permite o envio rápido de dados. No contexto de programação em Python, você empacota os dados
(payload) em uma mensagem e os envia usando a biblioteca socket.

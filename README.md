# 🏦 Gerenciamento de Conta Bancária

Este é um script Python que simula um sistema básico de gerenciamento de conta bancária. Ele permite que os usuários realizem depósitos, saques (limitados a três transações), visualizem o histórico de transações (extrato) e saiam do programa.

## 🚀 Primeiros Passos

Para utilizar este sistema de gerenciamento de conta bancária, siga as instruções abaixo:

### Pré-requisitos ✅

- Python 3.x instalado no seu sistema.

### Executando o Programa ▶️

1. Copie e cole o código Python fornecido em um novo arquivo Python (por exemplo, `gerenciamento_conta.py`).
2. Salve o arquivo e execute-o usando o interpretador Python.
3. O programa exibirá um menu com opções para depósito, saque, visualizar histórico de transações e sair do programa.
4. Siga as instruções na tela para interagir com o programa.

## Recursos 🛠️

### Depósito 💰

A opção "d" permite que o usuário faça um depósito em sua conta bancária. Informe o valor desejado para o depósito, e o saldo será atualizado de acordo.

### Saque 💸

A opção "s" permite que o usuário faça um saque em sua conta bancária. O usuário tem direito a três saques (LIMITE_SAQUES) por dia. O valor do saque não deve exceder o saldo da conta ou o limite especificado.

### Visualizar Histórico de Transações 📜

A opção "e" permite que o usuário visualize o histórico de transações (extrato), que mostra os depósitos e saques realizados na conta.

### Sair 🚪

A opção "q" permite que o usuário saia do programa.

## Exemplo de Uso 📝

```python
# Interação de exemplo com o programa
# O usuário faz um depósito, depois um saque e verifica o histórico de transações antes de sair.

======= menu =======
Saldo: R$ 0.00

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> d
Informe o valor a ser depositado: 100
Deposito no valor de 100.00 realizado com sucesso
======= menu =======
Saldo: R$ 100.00

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> s
Você tem 3 disponíveis
Lembrando que o limite de saque é de R$ 500
Qual o valor a ser sacado? 
50
sacando...
======= menu =======
Saldo: R$ 50.00

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> e
+100.00 Deposito na conta.
 Saldo atual: R$ 100.00.
-50.00    Saque na conta.
 Saldo atual: R$ 50.00.

[1] Fechar
=> 1
======= menu =======
Saldo: R$ 50.00

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> q
```

## Observação 🚧

Esta é uma simulação básica para fins educacionais e não inclui recursos de segurança ou armazenamento de dados. Em uma aplicação bancária real, é necessário considerar medidas de segurança e armazenar informações de conta de forma segura.

Certifique-se de entender o código e adaptá-lo ao seu caso de uso específico, se necessário.

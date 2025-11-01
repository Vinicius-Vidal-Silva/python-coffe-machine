☕ Simulador de Máquina de Café em Python

Este é um projeto de console em Python que simula o funcionamento de uma máquina de café. O script gerencia um inventário de recursos (água, leite, café), processa pagamentos com fichas (moedas), verifica o estoque disponível e "serve" o café solicitado pelo usuário.

O projeto é estruturado utilizando Programação Orientada a Objetos (POO) para gerenciar o estado da máquina e as diferentes bebidas.

✨ Funcionalidades

    Seleção de 3 tipos de café: Espresso, Latte e Cappuccino.

    Verificação de Recursos: A máquina confere automaticamente se há água, leite e grãos de café suficientes para preparar a bebida selecionada.

    Processamento de Pagamento: O usuário pode inserir "fichas" (moedas) virtuais nos valores de R$ 1.00, R$ 0.50 e R$ 0.25.

    Cálculo de Troco: O sistema calcula e informa o troco exato caso o valor inserido seja maior que o preço do café.

    Atualização de Estoque (Inventário): Após uma venda bem-sucedida, os ingredientes utilizados são deduzidos do estoque total da máquina.

    Contabilidade: O dinheiro de cada venda é adicionado ao caixa da máquina.

    Loop de Execução: A máquina funciona continuamente, pronta para o próximo cliente, até que o operador decida parar a execução.

📂 Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

    resources.py: Um arquivo de configuração que armazena dicionários Python contendo:

        cafes: As receitas de cada bebida (ingredientes e preço).

        recursos: O estoque inicial de ingredientes e o caixa da máquina.

        recurso_usuario: Um modelo para o "porta-fichas" do usuário (usado para iniciar o pagamento).

    main.py (ou seu arquivo principal): Contém toda a lógica da aplicação, incluindo:

        Classes:

            Cafe: Modela uma bebida com seus atributos (água, leite, etc.).

            Recurso: Modela o inventário da máquina.

            RecursoUsuario: Modela o "porta-fichas" do cliente para o pagamento.

        Funções:

            iniciar(): Exibe o menu e captura a escolha do usuário.

            cafe_escolhido(): Verifica se o café selecionado é válido e se há recursos.

            verificar_recursos(): Valida o estoque contra a receita.

            processar_pagamento(): Solicita as fichas, calcula o total e o troco.

            atualizar_recursos(): Deduz o estoque e adiciona o dinheiro ao caixa.

        Loop Principal: O while que mantém a máquina funcionando.

🛠️ Tecnologias Utilizadas

    Python 3.x

        Programação Orientada a Objetos (POO)

        Estruturas de dados (Dicionários e Listas)

🚀 Como Executar

    Clone o repositório:
    Bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git

Navegue até o diretório:
Bash

cd nome-do-repositorio

Execute o script principal: (Assumindo que seu arquivo principal se chama main.py)
Bash

python main.py

Siga as instruções no terminal para escolher seu café e inserir as fichas. Para encerrar, digite "2" (ou o comando de saída) quando perguntado.

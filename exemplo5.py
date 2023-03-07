## Olá bem vindos! Ao material de Estudo, sou Estevan, e venho apresentar a linguagem de programação 
## Python, para poder realizar o passo a passo, primeiro você precisa instalar o Python no seu computador
## Em seguida deverá baixar algum editor de Código, no meu caso uso VSCode. Lembrando, um código pode ser
## feito até no bloco de nota, mas só sera executado se conter no final .py para o computador poder saber]
## como ele deverá efetuar a leitura do arquivo.

## Para o primeiro exemplo de Python vou utilizar um exercicio de lógica apresentado pela professora.
## O código será bem comentado e bem explicativo.

## Para iniciarmos algum código em Python não precisamos colocar ALGORITIMO, na verdade é bem simples
# basta começar o seu código.
# vou usar o exercicio 5 para demonstrar!

## VAR
## Declaração de variavel é bem simples, basta fazer o seguinte.
quilowatt = 0

## De uma maneira bem simples, já colocamos e o Escreva (Input), e o Leia (quilowatt = )
## desta maneira já iremos receber a quantidade de QuiloWatt;
quilowatt = input("Digite o numero de consuto em KWh : ")

## Vamos iniciar a programação condicional do nosso código. Para poder-mos, efetuar os 
## calculos em determinados casos.
## para iniciar as condicoes, basta usar IF que traduzindo ficaria SE, igual no VisuAlg.

KWh = int(quilowatt)
## Para podermos utilizar a estrutura condicional, precisamos transformar o quilowatt
## em um numero, para verificar se é maior ou menor que o esperado.
if KWh < 30:
    ## Essa condicional irá verificar SE KWh é MENOR que 30 então, multiplicaremos pelo numero X
    totConta = KWh * 0.22366
    print("Você ira pagar: R$",totConta)


## Essa condicional irá testar SE o KWh é MAIOR OU IGUAL a 30
if KWh >= 30:
    ## Aqui estamos multiplicando a variavel totConta, para receber o total da conta do usuario.
    totConta = KWh * 0.38342

    ## Uma condicionao verificando se o valor da conta é maior que 100 reais.
    if totConta > 100:

        ## Descobrindo o valor do desconto que será aplicado no valor total da conta
        desconto = totConta * 0.04

        ## Calculando o valor total da conta com o desconto.
        totContaDes = totConta - desconto

        ## Vamos escrever na tela, O Quanto Deveria pagar sem desconto, Valor do Desconto e a %,
        ## e o Valor Atualizado com desconto.
        print("Você deveria pagar : R$",totConta, 
              "\nDesconto (4%): R$", desconto,
              "\nValor Atualizado : R$",totContaDes)
        
    ## Caso o valor de CONSUMO NÃO SEJA MAIOR QUE 100 Reais.
    ## Ele só ira escrever o Valor da conta
    else:
        print("Você irá pagar: R$", totConta)

## Bom m'amis. Esse foi o exercicio 5 da aula de lógica, e caso vcs tenham alguma dúvida sobre oque foi
## demonstrado, me mande alguma mensagem, ou algo do tipo que eu auxilio vcs.
## aplicando os mesmos conceitos de lógica, no visualg você ira conseguir solucionar o exercicio.
## Fica o desafio, traduzir para o visualg para melhor compreenção so que foi passado.
## Forte abraço.
## By Estevan Generoso.
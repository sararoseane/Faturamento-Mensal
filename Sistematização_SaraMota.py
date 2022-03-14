{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Sistematização_SaraMota.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Sara Roseane Silva Mota\n",
        "Matrícula: 72200223"
      ],
      "metadata": {
        "id": "TNlcW6LHjfn4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Definindo os salários fixos\n",
        "salario_fixo_vendedor = 1000.00\n",
        "salario_fixo_gerente = 2000.00\n",
        "\n",
        "#Definindo os funcionários para uma melhor manipulação\n",
        "no_funcionario = ['Emily (vendedora)', 'Larissa (vendedora)', 'Rafael (vendedor)', 'Milena (vendedora)']\n",
        "no_gerente = ['Jessica (gerente)']\n",
        "\n",
        "#Criando lista de vendas efetuadas pelos vendedores\n",
        "vendas_efetuadas = list()\n",
        "for i in no_funcionario:\n",
        "    # Capturando e tratando os valores digitados\n",
        "      while True:\n",
        "        try:\n",
        "            venda = float(input(f'Digite as vendas mensais do(a) {i}: '))\n",
        "            if venda < 0:\n",
        "                print('\\033[31m[31mValor INVÁLIDO! Digite apenas valores maiores ou iguais a \"0\":\\033[m')\n",
        "            break\n",
        "        except:\n",
        "            print('\\033[31mValor INVÁLIDO! Digite apenas valores reais!\\033[m')\n",
        "\n",
        "#Armazenando os valores digitados na lista vendas efetuadas\n",
        "      vendas_efetuadas.append(venda)\n",
        "\n",
        "#Calculando o faturamento total da loja\n",
        "faturamento = sum(vendas_efetuadas)\n",
        "print(f'Faturamento total = R$ {faturamento:.2f}'.replace('.',','))\n",
        "\n",
        "#Criando uma lista dos salários\n",
        "salario = list()\n",
        "\n",
        "#Calculando os salários dos vendedores e exibindo na tela\n",
        "cont = 0\n",
        "for i in vendas_efetuadas:\n",
        "    cont += 1\n",
        "    if i <= 5000:\n",
        "        salario_vendedor = (i * 0.01) + salario_fixo_vendedor\n",
        "        print(f'Salário do(a) {no_funcionario[cont-1]} = R$ {salario_vendedor:.2f}'.replace('.',','))\n",
        "\n",
        "    elif i > 5000 and i <= 10000:\n",
        "       salario_vendedor = (i * 0.015) + salario_fixo_vendedor\n",
        "       print(f'Salário do(a) {no_funcionario[cont-1]}  = R$ {salario_vendedor:.2f}'.replace('.',','))\n",
        "    \n",
        "    elif i > 10000:\n",
        "       salario_vendedor = (i * 0.02) + salario_fixo_vendedor\n",
        "       print(f'Salário do(a) {no_funcionario[cont-1]}  = R$ {salario_vendedor:.2f}'.replace('.',','))\n",
        "\n",
        "#Armazenando os salarios dos vendedores na lista salário     \n",
        "    salario.append(salario_vendedor)   \n",
        "\n",
        "#Calculando salário do gerente e exibindo na tela\n",
        "salario_gerente = (faturamento * 0.005) + salario_fixo_gerente\n",
        "print(f'Salário do(a) {no_gerente[0]} = R$ {salario_gerente:.2f}'.replace('.',','))\n",
        "\n",
        "#Calculando salário total dos funcionários e exibindo na tela\n",
        "salario_total_vendedor = sum(salario)   \n",
        "salario_total = salario_total_vendedor + salario_gerente\n",
        "print(f'Total dos salários = R$ {salario_total:.2f}'.replace('.',','))\n",
        "\n",
        "        \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TwttV7KSjm-x",
        "outputId": "bb05a1c8-b296-4bcc-f0e7-b7f8c9799d8e"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite as vendas mensais do(a) Emily (vendedora): 5890.8\n",
            "Digite as vendas mensais do(a) Larissa (vendedora): 10500.8\n",
            "Digite as vendas mensais do(a) Rafael (vendedor): 11235.96\n",
            "Digite as vendas mensais do(a) Milena (vendedora): 3500\n",
            "Faturamento total = R$ 31127,56\n",
            "Salário do(a) Emily (vendedora)  = R$ 1088,36\n",
            "Salário do(a) Larissa (vendedora)  = R$ 1210,02\n",
            "Salário do(a) Rafael (vendedor)  = R$ 1224,72\n",
            "Salário do(a) Milena (vendedora) = R$ 1035,00\n",
            "Salário do(a) Jessica (gerente) = R$ 2155,64\n",
            "Total dos salários = R$ 6713,74\n"
          ]
        }
      ]
    }
  ]
}

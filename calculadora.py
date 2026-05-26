import math
from flask import render_template, request


def calcular():
    try:
        num1_valor = request.form.get("num1", "").strip()
        if not num1_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o primeiro número.",
                resultados="",
            )
        num1 = float(num1_valor)
        operacao = request.form["operacao"]

        if operacao == "sqrt":
            if num1 < 0:
                resultado = "Erro"
                etapas = f"Não existe raiz real de {num1}."
                resultados = "Raiz de número negativo é indefinida nos reais."
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"
                resultados = resultado

        elif operacao == "log":
            if num1 <= 0:
                return render_template(
                    "calculadora.html",
                    etapas="Erro: logaritmo indefinido para número ≤ 0.",
                    resultados="",
                )
            resultado = math.log(num1)
            etapas = f"ln({num1}) = {resultado}"
            resultados = resultado

        else:
            num2_valor = request.form.get("num2", "").strip()
            if not num2_valor:
                return render_template(
                    "calculadora.html",
                    etapas="Informe o segundo número para esta operação.",
                    resultados="",
                )
            num2 = float(num2_valor)

            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"

            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"

            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} × {num2} = {resultado}"

            elif operacao == "/":
                if num2 == 0:
                    return render_template(
                        "calculadora.html",
                        etapas="Erro: divisão por zero é indefinida.",
                        resultados="",
                    )
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"

            elif operacao == "**":
                resultado = num1 ** num2
                etapas = f"{num1} ^ {num2} = {resultado}"

            else:
                return render_template(
                    "calculadora.html",
                    etapas="Operação inválida.",
                    resultados="",
                )

            resultados = resultado

        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultados,
        )

    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Erro: insira números válidos.",
            resultados="",
        )
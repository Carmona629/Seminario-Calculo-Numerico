import numpy as np
import matplotlib.pyplot as plt


def Euler(a: int, b: int, alfa: float, n: int):
    h = (b - a) / n  # passo

    # t[0]
    t = []
    t.append(a)

    # y[0]
    y = []
    y.append(alfa)

    # f(t[0], y[0])
    f = [0] * (n + 1)
    f[0] = 9.8 - 0.2 * y[0]  # fornecido pelo PVI

    # y exato
    y_exato = []
    y_exato.append(49 * (1 - np.e ** (-0.2 * t[0])))  # fórmula exata

    # erro
    erro = []
    erro.append(0)  # ((y_exato[0] - y[0]) / y_exato[0])

    for i in range(1, n + 1):
        t.append(t[i - 1] + h)
        y.append(y[i - 1] + h * f[i - 1])

        f[i] = 9.8 - 0.2 * y[i]

        y_exato.append(49 * (1 - np.e ** (-0.2 * t[i])))  # fórmula exata

        erro.append(abs(((y_exato[i] - y[i]) / y_exato[i])))  # fornecido pelo PVI

    # plot gráfico
    plt.subplot(1, 2, 1)
    plt.title("Gráfico y x t")
    plt.xlabel("t")
    plt.ylabel("v")
    plt.plot(t, y, color="red", marker="o", linestyle="--")  # y_aprox
    plt.plot(t, y_exato)  # y_exato
    plt.legend(["y_aprox", "y_exato"])

    # plot tabela
    plt.subplot(1, 2, 2).axis("off")
    data = [["ti", "y_aprox", "y_exato", "Er"]]
    for i in range(0, n + 1):
        data.append(
            [
                f"{t[i]:.3f}",
                f"{y[i]:.3f}",
                f"{y_exato[i]:.3f}",
                f"{erro[i]:.3f}",
            ]
        )
    table = plt.table(cellText=data, loc="center", cellLoc="center")
    # Ajustar o layout da tabela
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 0.75)  # Ajustar a escala conforme necessário

    plt.tight_layout()
    plt.show()


Euler(0, 16, 0, 16)

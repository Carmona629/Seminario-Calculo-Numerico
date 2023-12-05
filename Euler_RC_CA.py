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
    f[0] = 1350 * np.cos(60 * t[0]) - (y[0] / 16)  # fornecido pelo PVI

    # erro
    erro = []
    erro.append(0)  # ((y_exato[0] - y[0]) / y_exato[0])

    for i in range(1, n + 1):
        t.append(t[i - 1] + h)
        y.append(y[i - 1] + h * f[i - 1])

        f[i] = 1350 * np.cos(60 * t[i]) - (y[i] / 16)

    # plot gráfico
    plt.subplot(1, 2, 1)
    plt.title("Gráfico i(t) x t [s]")
    plt.xlabel("t[s]")
    plt.ylabel("i(t)")
    plt.plot(t, y, color="red", marker="o", linestyle="--")  # y_aprox

    # plot tabela
    plt.subplot(1, 2, 2).axis("off")
    data = [["ti", "i_aprox"]]
    for i in range(0, n + 1):
        data.append([f"{t[i]:.3f}", f"{y[i]:.3f}"])
    table = plt.table(cellText=data, loc="center", cellLoc="center")
    # Ajustar o layout da tabela
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 0.75)  # Ajustar a escala conforme necessário

    plt.tight_layout()
    plt.show()


Euler(a=0, b=10, alfa=0, n=20)

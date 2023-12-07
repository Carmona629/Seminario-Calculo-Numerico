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
    f[0] = -y[0] / 16  # fornecido pelo PVI

    # y exato
    y_exato = []
    y_exato.append(48)  # y[0] + h * (-3 * np.e ** (-t[0] / 16)))  # fórmula exata
    print(y[0])
    print(h)
    print(-3 * np.e ** (-t[0] / 16))
    # print(y_exato)

    # erro
    erro = []
    erro.append(0)  # (y_exato[0] - y[0]) / y_exato[0])

    for i in range(1, n + 1):
        k1 = f[i - 1]
        k2 = -(y[i - 1] + (h / 2) * k1) / 16
        k3 = -(y[i - 1] + (h / 2) * k2) / 16
        k4 = -(y[i - 1] + h * k3) / 16

        t.append(t[i - 1] + h)
        y.append(y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))

        f[i] = -y[i] / 16

        y_exato.append(y[i] + h * (-3 * np.e ** (-t[i] / 16)))  # fórmula exata

        erro.append(abs(((y_exato[i] - y[i]) / y_exato[i])))  # fornecido pelo PVI

    # plot gráfico
    # plt.subplot(1, 2, 1)
    plt.figure()
    plt.title("Gráfico i(t) [mA] x t [s]")
    plt.xlabel("t[s]")
    plt.ylabel("i(t)")
    plt.plot(t, y, color="red", marker="o", linestyle="--")  # y_aprox
    plt.plot(t, y_exato)  # y_exato
    plt.legend(["y_aprox", "y_exato"])

    # plot tabela
    # plt.subplot(1, 2, 2).axis("off")
    plt.figure()
    data = [["ti", "i_aprox", "i_exato", "Er"]]
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


Euler(a=0, b=100, alfa=48, n=500)

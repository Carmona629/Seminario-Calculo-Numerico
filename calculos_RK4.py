i0 = 48
h = 0.5

for i in range(0, 2):
    print(f"Para i_{i+1}")
    print(f"{i0:.3f}")

    k1 = -i0 / 16
    print(f"k1 = {k1:.3f}")

    k2 = -(i0 + (h / 2) * k1) / 16
    print(f"{(i0 + (h / 2) * k1):.3f}")
    print(f"k2 = {k2:.3f}")

    k3 = -(i0 + (h / 2) * k2) / 16
    print(f"{(i0 + (h / 2) * k2):.3f}")
    print(f"k3 = {k3:.3f}")

    k4 = -(i0 + h * k3) / 16
    print(f"{(i0 + h * k3):.3f}")
    print(f"k4 = {k4:.3f}")

    i0 = i0 + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    print(f"{i0:.3f}\n")

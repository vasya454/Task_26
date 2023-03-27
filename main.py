from math import sqrt
import matplotlib.pyplot as plt

if __name__ == '__main__':
    input_file = open("INPUT.TXT", "r")
    circum1 = input_file.readline()
    circum2 = input_file.readline()
    a1 = float(circum1.split(' ')[0])
    b1 = float(circum1.split(' ')[1])
    r1 = float(circum1.split(' ')[2])
    a2 = float(circum2.split(' ')[0])
    b2 = float(circum2.split(' ')[1])
    r2 = float(circum2.split(' ')[2])
    input_file.close()
    figure, axes = plt.subplots()
    c1 = plt.Circle((a1, b1), r1, fill=False)
    c2 = plt.Circle((a2, b2), r2, fill=False)
    axes.set_aspect(1)
    axes.add_artist(c1)
    axes.add_artist(c2)
    limx1 = min({a1 + r1, a2 + r2, a1 - r1, a2 - r2})
    limx2 = max({a1 + r1, a2 + r2, a1 - r1, a2 - r2})
    limy1 = min({b1 + r1, b2 + r2, b1 - r1, b2 - r2})
    limy2 = max({b1 + r1, b2 + r2, b1 - r1, b2 - r2})
    near = max({r1, r2}) * 0.05
    plt.xlim(limx1 - near, limx2 + near)
    plt.ylim(limy1 - near, limy2 + near)
    d = sqrt((b2 - b1) * (b2 - b1) + (a2 - a1) * (a2 - a1))
    if r2 + r1 >= d >= abs(r2 - r1):
        out_str = 'YES'
        message = 'Окружности пересекаются'
    else:
        out_str = 'NO'
        message = 'Окружности не пересекаются'
    plt.title(message)
    plt.show()

    output_file = open("OUTPUT.TXT", "w")
    output_file.write(out_str)

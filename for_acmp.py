from math import sqrt

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

d = sqrt((b2 - b1) * (b2 - b1) + (a2 - a1) * (a2 - a1))
if r2 + r1 >= d >= abs(r2 - r1):
    out_str = 'YES'
else:
    out_str = 'NO'
output_file = open("OUTPUT.TXT", "w")
output_file.write(out_str)

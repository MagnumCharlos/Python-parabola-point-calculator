
import matplotlib.pyplot as plt

x = 1
y = 1
a = int(input("a = "))
x_exp = int(input("exponent = "))
c = int(input("c = "))
forloop = int(input("how many loops"))
y_list = [0]
#neg_y_list = []

# for i in range(1, forloop):
#     x = y ** x_exp
#     res = a * x + c
#     neg_y_list.append(res * -1)
#     print(neg_y_list)
#     y = y+1

for i in range(1, forloop):
    x = y ** x_exp
    res = a * x + c
    y_list.append(res)
    print(y_list)
    y = y+1



y2 = 0

neg_x_list = [0]
x_list = [0]
for i in range(1, forloop):
    y2 = y2 +1
    neg_x_list.append(y2 * -1)

y2 = y2 -y2 +1

for i in range(1, forloop):
    y2 = y2 +1
    x_list.append(y2)



# Print the list
print(neg_x_list)

# neg_x_list = x_list
# neg_y_list = y_list

# for val in neg_x_list:
#     val * -1
# for val in neg_y_list:
#     val * -1


plt.plot(neg_x_list, y_list, x_list, y_list)
plt.plot()
plt.show()
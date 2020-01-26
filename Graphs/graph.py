import matplotlib.pyplot as plt
#with open('analysis.txt', 'r') as f:
    #lines = f.readlines()
    #x = [float(line.split()[0]) for line in lines]
    #y = [float(line.split()[1]) for line in lines]
x=[1, 2, 3, 4, 5]
y=[25, 21, 26, 20, 28]
#plt.plot(y ,x)

plt.bar(x, y, width=0.7, bottom=None, align='center')
plt.xlabel('Rating')
plt.ylabel('Number of books')
plt.title('Number of books per rating')
plt.show()
print(25+21+26+20+28)

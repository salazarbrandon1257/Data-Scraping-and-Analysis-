import matplotlib.pyplot as plt
with open('analysis.txt', 'r') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]

plt.plot(x, y)

#plt.bar(x, y, width=0.7, bottom=None, align='center')
plt.xlabel('Price')
plt.ylabel('Rating') 
plt.title('Book Price vs Rating')
plt.show()
#print(25+21+26+20+28)

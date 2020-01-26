import matplotlib.pyplot as plt
#with open('analysis.txt', 'r') as f:
 #   lines = f.readlines()
  #  x = [float(line.split()[0]) for line in lines]
   # y = [float(line.split()[1]) for line in lines]
x=[1, 2, 3, 4, 5]
y=[35.34, 36.21, 37.19, 33.34, 31.27]
#plt.plot(x, y)

plt.bar(x, y, width=0.7, bottom=None, align='center')
plt.xlabel('Rating')
plt.ylabel('Average Price') 
plt.title('Average Book Price per rating')
plt.show()
#print(25+21+26+20+28)

import matplotlib.pyplot as plt
#Here I just used the straight data I scraped, I just used the two columns I cared about
with open('analysis.txt', 'r') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]

plt.plot(x, y)
plt.xlabel('Price')
plt.ylabel('Rating') 
plt.title('Book Price vs Rating')
plt.show()

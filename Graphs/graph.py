import matplotlib.pyplot as plt
#to find the y values I used SQL to count the number of books per rating
x=[1, 2, 3, 4, 5]
y=[25, 21, 26, 20, 28]

plt.bar(x, y, width=0.7, bottom=None, align='center')
plt.xlabel('Rating')
plt.ylabel('Number of books')
plt.title('Number of books per rating')
plt.show()

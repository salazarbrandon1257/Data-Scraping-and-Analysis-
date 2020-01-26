import matplotlib.pyplot as plt
#I used SQL to find the average price per rating for the y values
x=[1, 2, 3, 4, 5]
y=[35.34, 36.21, 37.19, 33.34, 31.27]

plt.bar(x, y, width=0.7, bottom=None, align='center')
plt.xlabel('Rating')
plt.ylabel('Average Price') 
plt.title('Average Book Price per rating')
plt.show()


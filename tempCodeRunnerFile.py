x = np.linspace(1, 10, 100)
y_mergesortbigo = (x * np.log(x))-(x-1)
y_insertionsortbigo = (x**2+x-2)/4

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y_mergesortbigo, label='y = (x * log(x))-(x-1)', color='blue')
plt.plot(x, y_insertionsortbigo, label='y = (x**2+x-2)/4', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = (x * log(x))-(x-1) and y = (x**2+x-2)/4')
plt.grid(True)
plt.legend()
plt.show()
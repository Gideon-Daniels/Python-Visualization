import matplotlib.pyplot as plt

sizes = [25, 20, 45, 10]
labels = ["Cats", "Dogs", "Tigers", "Goats"]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct="%.2f")  # float and percentage value
# auto # num # aspect ratio
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

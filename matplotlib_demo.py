import matplotlib.pyplot as plt
# Import PdfPages
from matplotlib.backends.backend_pdf import PdfPages
from scipy import stats
import numpy as np


y=[261.3, 258.1 , 254.2 , 257.7 , 237.9 , 255.8 , 241.4 , 256.8 , 255.3 , 255 , 259.4 , 270.5 , 270.7 , 272.6 , 272.2 , 251.1 , 232.1 , 273 , 266.6 , 273.2 , 265.7 , 264.5 , 245.5 , 280.3 , 248.3 , 267 , 271.5 , 240.8 , 268.9 , 263.5 , 262.2 , 244.8 , 279.6 , 272.7 , 278.7 , 255.8 , 276.1 , 274.2 , 267.4 , 244.5 , 252 , 264 , 247.7 , 273.6 , 264.5 , 285.3 , 277.8 , 261.4 , 253.6 , 278.5 , 260 , 271.2 , 254.8 , 256.1 , 264.5 , 255.4 , 259.5 , 274.9 , 272.1 , 273.3 , 279.3 , 279.8 , 272.8 , 268.5 , 283.7 , 263.2 , 257.5 , 233.7 , 260.2 , 263.7 , 244.3 , 241.2 , 254.4 , 274 , 260.7 , 260.6 , 255.1 , 233.7 , 253.7 , 250.2 , 251.4 , 270.6 , 273.4 , 242.9 , 276.6 , 237.8 , 261 , 236 , 251.8 , 280.3 , 268.3 , 266.8 , 254.5 , 234.3 , 251.6 , 226.8 , 240.5 , 252.1 , 245.6 , 270.5 ]
x=range(1,len(y)+1)

plt.figure()

plt.subplot(331)
plt.plot(x,y)
plt.title("Plot")

plt.subplot(332)
plt.plot(x,y,'ro')
plt.title("Dot Plot")


plt.subplot(333)
plt.bar(x,y)
plt.title("Bar Plot")


plt.subplot(334)
plt.scatter(x,y)
plt.title("Scatter Plot")


plt.subplot(335)
# the histogram of the data
n, bins, patches = plt.hist(y,50)
plt.title("Histogram")


plt.subplot(336)
plt.boxplot(y)
plt.title("Box Plot")


plt.subplot(337)
stats.probplot(y, plot=plt)
plt.title("Q-Q Plot")


plt.subplot(338)

#test = stats.norm.rvs(loc=0, scale=1, size=100)
#stats.probplot(test, plot=plt)
np.random.seed(seed=0)
x = np.random.randn(1000)
y = np.random.randn(100)
z = np.random.randn(10)

plt.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
           labels=('x', 'y', 'z'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.title("Box Plot")

plt.subplot(339)
x, y, z = 128, 256, 1024
plt.pie((x, y, z), labels=('x', 'y', 'z'), autopct='%1.1f%%')
plt.title("Pie Chart")

plt.show()


## Save the diagram to the PDF

# Initialize the pdf file
pp = PdfPages('multipage.pdf')

# Save the figure to the file
pp.savefig()

# Close the file
pp.close()



import matplotlib.pyplot as plt
import numpy as np

nums = [0.5, 0.7, 1., 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

a = np.histogram(nums, bins)

print(a)

plt.hist(nums, bins)
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.title("Histogram of nums against bins")
plt.show()

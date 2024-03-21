import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
iq_score = np.random.normal(loc=100, scale=15, size=10000)
min_iq = 50
max_iq = 350
bin_width = 5
num_bins = int((max_iq-min_iq)/bin_width)
plt.hist(iq_score, bins=range(min_iq, max_iq, bin_width), color="red", alpha=0.7)

plt.xlabel('IQ scores')
plt.ylabel('Frequency In the Global Population')
plt.title("Histogram representing average global IQ scores")
plt.grid(True)
plt.show()
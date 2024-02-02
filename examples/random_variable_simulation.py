# random variable simulation

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, cauchy

# Random Variables with Uniform Distribution in an interval of values:
min_interval = -5
max_interval = 7
Y = min_interval + np.random.rand(N, 1) * (max_interval - min_interval)

plt.figure()
plt.hist(Y, bins=Q, density=True)
plt.title("Random Variables with Uniform Distribution in an interval of values")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()

# Gaussian Distribution:
mu = 1
ds = 3
Z = mu + ds * np.random.randn(N, 1)

plt.figure()
plt.hist(Z, bins=Q, density=True, alpha=0.6)
line = np.linspace(min(Z), max(Z), N)
theoretical = norm.pdf(line, mu, ds)
plt.plot(line, theoretical, 'r', linewidth=2, label='Theoretical')
plt.title('Histogram of Gaussian Distribution')
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.show()

# Cauchy Distribution:
X_cds = mu + ds * np.tan(np.pi * (X - 0.5))

plt.figure()
plt.hist(X_cds, bins=Q, density=True, alpha=0.6)
line2 = np.linspace(min(X_cds), max(X_cds), N)
X_pdf = 1 / (np.pi * ds * (1 + ((line2 - mu) / ds) ** 2))
plt.plot(X_cds, X_pdf, label='Theoretical Cauchy')
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.title("Cauchy Distribution")
plt.legend()
plt.show()

# Statistics for Uniform Distribution:
N = 5000

media = np.zeros(N)
desvest = np.zeros(N)
skew = np.zeros(N)
exkurt = np.zeros(N)

S1, S2, S3, S4 = 0, 0, 0, 0

for i in range(1, N + 1):
    dist_p2 = min_interval + np.random.rand() * (max_interval - min_interval)
    S1 += dist_p2
    S2 += dist_p2 ** 2
    S3 += dist_p2 ** 3
    S4 += dist_p2 ** 4

    esp1 = S1 / i
    esp2 = S2 / i
    esp3 = S3 / i
    esp4 = S4 / i

    media[i - 1] = esp1
    desvest[i - 1] = np.sqrt(esp2 - esp1 ** 2)
    skew[i - 1] = (esp3 - 3 * esp2 * esp2 + 2 * esp1 ** 3)
    exkurt[i - 1] = (esp4 - 4 * esp3 * esp1 + 6 * esp2 * esp1 ** 2 - 3 * esp1 ** 4) - 3

plt.figure()
plt.subplot(2, 2, 1)
plt.plot(media)
plt.title("Mean")
plt.xlabel("N")
plt.ylabel("Mean")
plt.legend(["Mean"], loc="upper right")

plt.subplot(2, 2, 2)
plt.plot(desvest)
plt.title("Standard Deviation")
plt.xlabel("N")
plt.ylabel("Standard Deviation")
plt.legend(["Standard Deviation"], loc="upper right")

plt.subplot(2, 2, 3)
plt.plot(skew)
plt.title("Skewness")
plt.xlabel("N")
plt.ylabel("Skewness")
plt.legend(["Skewness"], loc="upper right")

plt.subplot(2, 2, 4)
plt.plot(exkurt)
plt.title("Excess Kurtosis")
plt.xlabel("N")
plt.ylabel("Excess Kurtosis")
plt.legend(["Excess Kurtosis"], loc="upper right")

plt.show()

# Statistics for Normal Distribution
media2 = np.zeros(N)
desvest2 = np.zeros(N)
skew2 = np.zeros(N)
exkurt2 = np.zeros(N)

S11, S22, S33, S44 = 0, 0, 0, 0

for j in range(1, N + 1):
    dist_p3 = mu + ds * np.random.randn()
    S11 += dist_p3
    S22 += dist_p3 ** 2
    S33 += dist_p3 ** 3
    S44 += dist_p3 ** 4

    esp11 = S11 / j
    esp22 = S22 / j
    esp33 = S33 / j
    esp44 = S44 / j

    media2[j - 1] = esp11
    desvest2[j - 1] = np.sqrt(esp22 - esp11 ** 2)
    skew2[j - 1] = (esp33 - 3 * esp22 * esp22 + 2 * esp11 ** 3)
    exkurt2[j - 1] = (esp44 - 4 * esp33 * esp11 + 6 * esp22 * esp11 ** 2 - 3 * esp11 ** 4) - 3

plt.figure()
plt.subplot(2, 2, 1)
plt.plot(media2)
plt.title("Mean")
plt.xlabel("N")
plt.ylabel("Mean")
plt.legend(["Mean"], loc="upper right")

plt.subplot(2, 2, 2)
plt.plot(desvest2)
plt.title("Standard Deviation")
plt.xlabel("N")
plt.ylabel("Standard Deviation")
plt.legend(["Standard Deviation"], loc="upper right")

plt.subplot(2, 2, 3)
plt.plot(skew2)
plt.title("Skewness")
plt.xlabel("N")
plt.ylabel("Skewness")
plt.legend(["Skewness"], loc="upper right")

plt.subplot(2, 2, 4)
plt.plot(exkurt2)
plt.title("Excess Kurtosis")
plt.xlabel("N")
plt.ylabel("Excess Kurtosis")
plt.legend(["Excess Kurtosis"], loc="upper right")

plt.show()

# Statistics for Cauchy Distribution
media3 = np.zeros(N)
desvest3 = np.zeros(N)
skew3 = np.zeros(N)
exkurt3 = np.zeros(N)

S111, S222, S333, S444 = 0, 0, 0, 0

for k in range(1, N + 1):
    dist_p4 = mu + ds * np.random.randn()
    S111 += dist_p4
    S222 += dist_p4 ** 2
    S333 += dist_p4 ** 3
    S444 += dist_p4 ** 4

    esp111 = S111 / k
    esp222 = S222 / k
    esp333 = S333 / k
    esp444 = S444 / k

    media3[k - 1] = esp111
    desvest3[k - 1] = np.sqrt(esp222 - esp111 ** 2)
    skew3[k - 1] = (esp333 - 3 * esp222 * esp222 + 2 * esp111 ** 3)
    exkurt3[k - 1] = (esp444 - 4 * esp333 * esp111 + 6 * esp222 * esp111 ** 2 - 3 * esp111 ** 4) - 3

plt.figure()
plt.subplot(2, 2, 1)
plt.plot(media3)
plt.title("Mean")
plt.xlabel("N")
plt.ylabel("Mean")
plt.legend(["Mean"], loc="upper right")

plt.subplot(2, 2, 2)
plt.plot(desvest3)
plt.title("Standard Deviation")
plt.xlabel("N")
plt.ylabel("Standard Deviation")
plt.legend(["Standard Deviation"], loc="upper right")

plt.subplot(2, 2, 3)
plt.plot(skew3)
plt.title("Skewness")
plt.xlabel("N")
plt.ylabel("Skewness")
plt.legend(["Skewness"], loc="upper right")

plt.subplot(2, 2, 4)
plt.plot(exkurt3)
plt.title("Excess Kurtosis")
plt.xlabel("N")
plt.ylabel("Excess Kurtosis")
plt.legend(["Excess Kurtosis"], loc="upper right")
plt.show()



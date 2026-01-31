import numpy as np
import matplotlib.pyplot as plt

# Time settings
t = np.linspace(0, 5, 2000)
dt = t[1] - t[0]

# Parameters
A = 1.0
zeta = 0.05
w = 10
wd = w * np.sqrt(1 - zeta**2)

# Damped vibration
x = A * np.exp(-zeta * w * t) * np.sin(wd * t)

# -------------------------
# 1️⃣ Save vibration signal
# -------------------------
plt.figure(figsize=(10,5))
plt.plot(t, x)
plt.title("Damped Vibration Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("vibration_signal.png", dpi=300)
plt.close()

# -------------------------
# 2️⃣ Add noise + save plot
# -------------------------
noise = 0.1 * np.random.randn(len(t))
x_noisy = x + noise

plt.figure(figsize=(10,5))
plt.plot(t, x_noisy, color='orange')
plt.title("Noisy Vibration Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("noisy_vibration_signal.png", dpi=300)
plt.close()

# -------------------------
# 3️⃣ FFT + save spectrum
# -------------------------
X = np.fft.fft(x_noisy)
freqs = np.fft.fftfreq(len(t), dt)

positive_freqs = freqs[:len(freqs)//2]
positive_X = np.abs(X[:len(X)//2])

plt.figure(figsize=(10,5))
plt.plot(positive_freqs, positive_X, color='green')
plt.title("Frequency Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.savefig("fft_spectrum.png", dpi=300)
plt.close()

print("All plots saved successfully!")

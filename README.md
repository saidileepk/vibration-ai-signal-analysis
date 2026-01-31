📌 Vibration Signal Analysis using Python
Damped Vibration Simulation | Noisy Signal Generation | FFT Spectrum Analysis

A mini-project for physics & engineering internship applications — demonstrates strong skills in signal processing, numerical computing, and data visualization.

🔍 Overview

This project performs fundamental vibration analysis using Python.
It covers:

Generating a damped vibration signal

Adding Gaussian noise

Computing the Fast Fourier Transform (FFT)

Visualizing:

Time-domain clean signal

Noisy vibration signal

Frequency spectrum

This project showcases skills in signal processing, NumPy, SciPy, Matplotlib, and scientific computing — useful for internship profiles (IITs, IISc, DRDO, BARC, CSIR labs, etc.).

📊 Results (Plots Included)
🔹 Time-Domain Vibration Signal

Clean damped oscillation.
(Generated plot: vibration_signal.png)

🔹 Noisy Vibration Signal

Added Gaussian noise to simulate realistic engineering-type measurements.
(Generated plot: noisy_vibration_signal.png)

🔹 Frequency Spectrum (FFT)

Shows dominant frequency peaks and noise distribution.
(Generated plot: fft_spectrum.png)

🚀 How to Run
1. Install dependencies
pip install numpy matplotlib

2. Run the main script
python vibration_full.py


This will automatically generate all plots in the folder.

📁 Project Structure
File	Purpose
vibration_full.py	Main Python script (signal generation + noise + FFT + plots)
vibration_signal.png	Clean vibration signal plot
noisy_vibration_signal.png	Noisy signal plot
fft_spectrum.png	Frequency spectrum (FFT)
.gitattributes	Git configuration file
README.md	Project documentation
📘 Theory Behind the Project (Short Summary)

A damped harmonic oscillator is modeled using:

x(t) = A * exp(-ζ * ω * t) * sin(ω * t)
Where:

A → amplitude

ζ → damping ratio

ω → natural frequency

t → time

Gaussian noise is added to simulate sensor-like disturbances
x_noisy(t) = x(t) + N(0, σ²)

The FFT converts the time-domain signal into frequency components

X(f) = Σ x(t) * exp(-j * 2π * f * t)

This represents the discrete Fourier transform where:
- `Σ` → summation over all time samples  
- `exp(−j2πft)` → complex sinusoidal basis  
- `f` → frequency  
- `t` → time  

🎯 Applications

This type of analysis is used in:

Mechanical vibration monitoring

Structural health analysis

Aerospace and automotive signal analysis

Research labs working on sensors & instrumentation

Physics and engineering internships

🤝 Contributions

Feel free to fork, modify, and contribute new ideas (filters, STFT, wavelets, etc.).

⭐ Support

If you find this useful, consider giving the repository a star 🌟 — it helps a lot!


# 🌡️ Thermal Diode Analyzer (Python Project)

This Python project simulates how **temperature affects diode performance** for both **Silicon** and **Germanium** diodes. It also calculates **power loss** in both types of diodes and plots everything for analysis.

## ✅ Features

- User inputs temperature & voltage range
- Simulates I-V curves for both diodes
- Calculates power loss = V × I
- Saves the output graph as `diode_iv_temp_power.png`
- Great for students and electronics project planning

## 📦 Installation

Install dependencies with:

```bash
pip install numpy matplotlib
```

## ▶️ Usage

```bash
python main.py
```

Then enter:

- Temperature in Kelvin (e.g., 300)
- Minimum voltage (e.g., -1)
- Maximum voltage (e.g., 1)

## 📈 Output

A dual plot will be generated:
1. I-V Curve: Silicon vs Germanium
2. Power Loss Curve

Saved as:
```
diode_iv_temp_power.png
```

## 🎯 Real-Life Application

- Energy-efficient circuit design
- Understanding temperature sensitivity of semiconductors
- Selection of diode type for outdoor or industrial use

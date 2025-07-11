import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19   # Electron charge (C)
k = 1.38e-23  # Boltzmann constant (J/K)
n = 1.0       # Ideality factor

# Recommended max power loss thresholds (in W)
threshold_silicon = 0.05  # 50 mW
threshold_germanium = 0.02  # 20 mW

# Ask user for temperature input
try:
    T = float(input("🔺 Enter temperature in Kelvin (e.g., 300): ").strip())
except:
    print("Invalid input. Using default T = 300K")
    T = 300

# Ask user for voltage range
try:
    V_min = float(input("🔻 Enter minimum voltage (e.g., -1): ").strip())
    V_max = float(input("🔼 Enter maximum voltage (e.g., 1): ").strip())
except:
    print("Invalid input. Using default range -1V to +1V")
    V_min = -1
    V_max = 1

V = np.linspace(V_min, V_max, 400)

# Diode saturation currents
Is_silicon = 1e-12
Is_germanium = 1e-6

# Diode equation
def diode_current(V, Is, T):
    return Is * (np.exp((q * V) / (n * k * T)) - 1)

# Calculate currents and power
I_silicon = diode_current(V, Is_silicon, T)
I_germanium = diode_current(V, Is_germanium, T)

# Clip currents for safety
I_silicon_clipped = np.clip(I_silicon, -1e-3, 1e-1)
I_germanium_clipped = np.clip(I_germanium, -1e-3, 1e-1)

# Power loss: P = V * I
P_silicon = V * I_silicon_clipped
P_germanium = V * I_germanium_clipped

# Max power loss values for alert
max_p_silicon = np.max(np.abs(P_silicon))
max_p_germanium = np.max(np.abs(P_germanium))

# Print recommendation notes
print("\n🔍 Power Loss Analysis at T = {} K:".format(T))
print(" - Silicon max power loss: {:.4f} W".format(max_p_silicon))
print(" - Germanium max power loss: {:.4f} W".format(max_p_germanium))

# Alert if exceeds recommended range
if max_p_silicon > threshold_silicon:
    print("⚠️ WARNING: Silicon diode power loss is too high! Consider cooling or changing design.")
else:
    print("✅ Silicon power loss is within ideal range (<= {:.2f} W)".format(threshold_silicon))

if max_p_germanium > threshold_germanium:
    print("⚠️ WARNING: Germanium diode power loss is too high! Consider replacing or reducing load.")
else:
    print("✅ Germanium power loss is within ideal range (<= {:.2f} W)".format(threshold_germanium))

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

axs[0].plot(V, I_silicon_clipped, label="Silicon Diode", color='blue')
axs[0].plot(V, I_germanium_clipped, label="Germanium Diode", color='green', linestyle='--')
axs[0].set_ylabel("Current (A)")
axs[0].set_title(f"I-V Characteristics at T = {T} K")
axs[0].legend()
axs[0].grid(True)

axs[1].plot(V, P_silicon, label="Silicon Power Loss", color='blue')
axs[1].plot(V, P_germanium, label="Germanium Power Loss", color='green', linestyle='--')
axs[1].set_xlabel("Voltage (V)")
axs[1].set_ylabel("Power (W)")
axs[1].set_title("Power Loss (P = V × I)")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.savefig("diode_iv_temp_power.png")
plt.show()

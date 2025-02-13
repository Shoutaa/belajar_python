import numpy as np
import matplotlib.pyplot as plt

# Data
data = [
    27.5, 33.0, 15.0, 44.7, 59.1, 41.5, 50.0, 49.0,
    40.8, 51.1, 47.9, 40.7, 66.3, 42.3, 46.8, 34.5,
    42.1, 29.0, 62.6, 58.5, 61.8, 38.5, 72.3, 58.1,
    23.9, 65.7, 44.8, 69.1, 66.4, 44.7, 59.6, 31.0,
    54.2, 56.8, 47.8, 38.8, 32.0, 43.8, 45.0, 60.5,
]

# Konversi data menjadi numpy array
data_np = np.array(data)

# Hitung mean, median, dan mode
mean_value = np.mean(data_np)
median_value = np.median(data_np)
mode_value = np.argmax(np.bincount(data_np.astype(int)))

# Diagram
plt.hist(data_np, bins=20, alpha=0.7, color='blue', edgecolor='black') # Menggunakan 20 bins

# Tambahkan garis untuk mean, median, dan mode
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(median_value, color='green', linestyle='dashed', linewidth=1, label='Median')
plt.axvline(mode_value, color='purple', linestyle='dashed', linewidth=1, label='Mode')

# Tambahkan legenda
plt.legend()
plt.title("Diagram")
plt.xlabel("Data")
plt.ylabel("Nilai")
# Tampilkan diagram
plt.show()

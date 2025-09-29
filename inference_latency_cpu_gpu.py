# Inference Latency: CPU vs GPU
import matplotlib.pyplot as plt
devices = ['CPU', 'GPU']
times = [1200, 150]
plt.bar(devices, times, color=['red', 'green'])
plt.title('Inference Latency: CPU vs GPU')
plt.ylabel('Latency (ms)')
plt.show()

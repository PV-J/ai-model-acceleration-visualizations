# Throughput vs Batch Size
batch_sizes = [1, 8, 16, 32, 64]
throughput = [50, 300, 550, 1000, 1800]
plt.plot(batch_sizes, throughput, marker='o')
plt.title('Throughput vs Batch Size')
plt.xlabel('Batch Size')
plt.ylabel('Samples per second')
plt.grid(True)
plt.show()


# Memory Usage: FP32 vs FP16
import seaborn as sns
import pandas as pd
data = pd.DataFrame({'Precision': ['FP32', 'FP16'], 'Memory Usage (MB)': [1500, 800]})
sns.barplot(x='Precision', y='Memory Usage (MB)', data=data)
plt.title('Memory Usage: FP32 vs FP16')
plt.show()


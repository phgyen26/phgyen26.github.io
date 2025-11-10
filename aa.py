import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
X = np.array([1, 2, 3])
y = np.array([2, 4, 5])

# Tính hệ số w, b bằng công thức hồi quy tuyến tính
w = np.sum((X - X.mean())*(y - y.mean())) / np.sum((X - X.mean())**2)
b = y.mean() - w * X.mean()

print(f"w = {w:.2f}, b = {b:.2f}")

# Vẽ đồ thị
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, w*X + b, color='red', label=f'y = {w:.2f}x + {b:.2f}')
plt.legend(); plt.grid(); plt.show()

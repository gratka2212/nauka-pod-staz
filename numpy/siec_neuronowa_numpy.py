import numpy as np
rng = np.random.default_rng(seed=42)

x = rng.normal(loc=50, scale=15, size=(100,4))

y_true = np.random.randint(2, size=(100,))

x_norm = (x - x.mean(axis=0))/x.std(axis=0)
# print(x_norm.mean(axis=0), x_norm.std(axis=0))

w = rng.normal(loc = 0, scale = 1, size = (4, 1))
b = 0.5
z = x_norm @ w + b

y_hat = (1/(1+np.exp(-z))).flatten()
y_pred = (y_hat>=0.5).astype(int)

acc = (y_pred == y_true).mean()
mse = (1/np.shape(y_true)[0])*np.sum((y_true-y_hat)**2)

print(f"Wymiary:\nx_norm: {np.shape(x_norm)}\nz: {np.shape(z)}\ny_hat: {np.shape(y_hat)}\n\n-------------------------\n\nAccuracy: {acc}\nMSE: {mse}")
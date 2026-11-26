import numpy as np
rng = np.random.default_rng(seed=42)

x = rng.normal(loc=50, scale=15, size=(100,4))

# y_true = rng
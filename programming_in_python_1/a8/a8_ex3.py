class StandardScaler:
    def __init__(self):
        self.mu = None
        self.sig = None


    def fit(self, features : list):
        self.mu = sum(features) / len(features)
        self.sig = (sum((x - self.mu) ** 2 for x in features) / (len(features) - 1)) ** (1/2)

    def transform(self, features : list):
        if self.mu is None or self.sig is None:
            raise ValueError("Scaler has not been fitted.")
        else:
            fitted_features = []
            for elem in features:
                fitted_features.append((elem - self.mu)/self.sig)
            return fitted_features

    def fit_transform(self, features : list):
        self.fit(features)
        return self.transform(features)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key == 0:
                return self.mu
            elif key == 1:
                return self.sig
            raise IndexError("Index out of range")
        raise TypeError("Indices must be integers")

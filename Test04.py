def numeroPositivo(X):
    X.sort()
    num_positivo = 1

    for num in X:
        if num <= num_positivo:
            num_positivo = num + 1

    return num_positivo


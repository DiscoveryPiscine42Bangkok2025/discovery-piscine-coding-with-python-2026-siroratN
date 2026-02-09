for i in range(11):
    results = [str(i * j) for j in range(11)]
    line = " ".join(results)
    print(f"Table de {i}: {line}")
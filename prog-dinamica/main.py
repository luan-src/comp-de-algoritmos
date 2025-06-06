import time
import pandas as pd
import matplotlib.pyplot as plt
import fibonacci_recursivo
import fibonacci_top_down
import fibonacci_bottom_up

resultados = {
    "n": [],
    "recursivo": [],
    "top_down": [],
    "bottom_up": []
}

for n in range(0, 41):
    resultados["n"].append(n)

    # Recursivo
    inicio = time.perf_counter()
    fibonacci_recursivo.fibonacci(n)
    fim = time.perf_counter()
    resultados["recursivo"].append((fim - inicio) * 1000)

    # Top-Down
    inicio = time.perf_counter()
    fibonacci_top_down.fibonacci(n)
    fim = time.perf_counter()
    resultados["top_down"].append((fim - inicio) * 1000)

    # Bottom-Up
    inicio = time.perf_counter()
    fibonacci_bottom_up.fibonacci(n)
    fim = time.perf_counter()
    resultados["bottom_up"].append((fim - inicio) * 1000)

df = pd.DataFrame(resultados)
df.to_csv("tempos_fibonacci.csv", index=False)
plt.figure(figsize=(10, 6))
plt.plot(df["n"], df["recursivo"], label="Recursivo", marker="o")
plt.plot(df["n"], df["top_down"], label="Top-Down (Memo)", marker="s")
plt.plot(df["n"], df["bottom_up"], label="Bottom-Up", marker="^")
plt.title("Tempo de execução das abordagens de Fibonacci (0 ≤ n ≤ 40)")
plt.xlabel("n (n-ésimo termo)")
plt.ylabel("Tempo (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

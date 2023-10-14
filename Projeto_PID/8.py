import tkinter as tk # biblioteca para interface gráfica

# Função para calcular o PID do CHR1
def calcular_pid_chr1():
    K = float(entry_K.get())
    t = float(entry_t.get())
    θ = float(entry_θ.get())
    
    chr1_kp = (0.6 * t) / (K * θ)
    chr1_ti = t
    chr1_td = 0.5 * θ
    
    result_label.config(text=f"CHR1 PID: Kp = {chr1_kp}, ti = {chr1_ti}, td = {chr1_td}")

# Função para calcular o PID do Cohen-Coon
def calcular_pid_cohen_coon():
    K = float(entry_K.get())
    t = float(entry_t.get())
    θ = float(entry_θ.get())
    
    cc_kc = (1 / K) * (t / θ) * (4 / 3 + (1 / 4) * (θ / t))
    cc_ti = θ * (32 + 6 * (θ / t)) / (13 + 8 * (θ / t))
    cc_td = θ * 4 / (11 + 2 * (θ / t))
    
    result_label.config(text=f"Cohen-Coon PID: Kc = {cc_kc}, ti = {cc_ti}, td = {cc_td}")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de PID")

# Cria um rótulo com o exemplo de valores
example_label = tk.Label(root, text="Exemplo K = 1, t = 2.125 e θ = 0.5")
example_label.grid(row=0, column=0, columnspan=2)  # Coloque-o na parte superior da janela

# Cria os rótulos e campos de entrada para os parâmetros
label_K = tk.Label(root, text="K:")
label_t = tk.Label(root, text="t:")
label_θ = tk.Label(root, text="θ:")
entry_K = tk.Entry(root)
entry_t = tk.Entry(root)
entry_θ = tk.Entry(root)

# Cria botões para calcular o PID
calculate_chr1_button = tk.Button(root, text="Calcular CHR1 PID", command=calcular_pid_chr1)
calculate_cohen_coon_button = tk.Button(root, text="Calcular Cohen-Coon PID", command=calcular_pid_cohen_coon)

# Rótulo para exibir o resultado
result_label = tk.Label(root, text="Para o resultado aparecer clique nas opções acima")

# Coloca os elementos na janela
label_K.grid(row=1, column=0)
label_t.grid(row=2, column=0)
label_θ.grid(row=3, column=0)
entry_K.grid(row=1, column=1)
entry_t.grid(row=2, column=1)
entry_θ.grid(row=3, column=1)
calculate_chr1_button.grid(row=4, column=0)
calculate_cohen_coon_button.grid(row=4, column=1)
result_label.grid(row=5, columnspan=2)

root.mainloop()
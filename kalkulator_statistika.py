import tkinter as tk
import statistics

def calculate_statistics():
    data = [float(x) for x in data_entry.get().split(",")]
    mean_value = statistics.mean(data)
    median_value = statistics.median(data)
    mode_value = statistics.mode(data)
    variance_value = statistics.variance(data)
    stdev_value = statistics.stdev(data)
    min_value = min(data)
    max_value = max(data)

    mean_formula = "Mean = {:.2f}".format(mean_value)
    median_formula = "Median = {:.2f}".format(median_value)
    mode_formula = "Mode = {:.2f}".format(mode_value)
    variance_formula = "Variance = {:.2f}".format(variance_value)
    stdev_formula = "Standard Deviation = {:.2f}".format(stdev_value)
    min_formula = "Minimum = {:.2f}".format(min_value)
    max_formula = "Maximum = {:.2f}".format(max_value)

    mean_formula_value.set(mean_formula)
    median_formula_value.set(median_formula)
    mode_formula_value.set(mode_formula)
    variance_formula_value.set(variance_formula)
    stdev_formula_value.set(stdev_formula)
    min_formula_value.set(min_formula)
    max_formula_value.set(max_formula)

root = tk.Tk()
root.title("Kalkulator Statistika")

# Label dan Entry untuk memasukkan data
data_label = tk.Label(root, text="Data:")
data_label.grid(row=0, column=0, padx=10, pady=10)

data_entry = tk.Entry(root, width=40)
data_entry.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk menghitung statistika
calculate_button = tk.Button(root, text="Hitung", command=calculate_statistics)
calculate_button.grid(row=0, column=2, padx=10, pady=10)

# Label dan Entry untuk menampilkan hasil statistika
mean_formula_label = tk.Label(root, text="Rata-rata:")
mean_formula_label.grid(row=1, column=0, padx=10, pady=5)

mean_formula_value = tk.StringVar()
mean_formula_entry = tk.Entry(root, textvariable=mean_formula_value, state="readonly")
mean_formula_entry.grid(row=1, column=1, padx=10, pady=5)

median_formula_label = tk.Label(root, text="Median:")
median_formula_label.grid(row=2, column=0, padx=10, pady=5)

median_formula_value = tk.StringVar()
median_formula_entry = tk.Entry(root, textvariable=median_formula_value, state="readonly")
median_formula_entry.grid(row=2, column=1, padx=10, pady=5)

mode_formula_label = tk.Label(root, text="Modus:")
mode_formula_label.grid(row=3, column=0, padx=10, pady=5)

mode_formula_value = tk.StringVar()
mode_formula_entry = tk.Entry(root, textvariable=mode_formula_value, state="readonly")
mode_formula_entry.grid(row=3, column=1, padx=10, pady=5)

variance_formula_label = tk.Label(root, text="Variansi:")
variance_formula_label.grid(row=4, column=0, padx=10, pady=5)

variance_formula_value = tk.StringVar()
variance_formula_entry = tk.Entry(root, textvariable=variance_formula_value, state="readonly")
variance_formula_entry.grid(row=4, column=1, padx=10, pady=5)

stdev_formula_label = tk.Label(root, text="Standar Deviasi:")
stdev_formula_label.grid(row=5, column=0, padx=10, pady=5)

stdev_formula_value = tk.StringVar()
stdev_formula_entry = tk.Entry(root, textvariable=stdev_formula_value, state="readonly")
stdev_formula_entry.grid(row=5, column=1, padx=10, pady=5)

min_formula_label = tk.Label(root, text="Nilai Minimum:")
min_formula_label.grid(row=6, column=0, padx=10, pady=5)

min_formula_value = tk.StringVar()
min_formula_entry = tk.Entry(root, textvariable=min_formula_value, state="readonly")
min_formula_entry.grid(row=6, column=1, padx=10, pady=5)

max_formula_label = tk.Label(root, text="Nilai Maksimum:")
max_formula_label.grid(row=7, column=0, padx=10, pady=5)

max_formula_value = tk.StringVar()
max_formula_entry = tk.Entry(root, textvariable=max_formula_value, state="readonly")
max_formula_entry.grid(row=7, column=1, padx=10, pady=5)

root.mainloop()

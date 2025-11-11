import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], selected_items

def visualize():
    try:
        values = list(map(int, value_entry.get().split(',')))
        weights = list(map(int, weight_entry.get().split(',')))
        capacity = int(capacity_entry.get())

        if len(values) != len(weights):
            messagebox.showerror("Error", "Values and Weights must be of same length!")
            return

        max_profit, selected = knapsack(values, weights, capacity)
        
        result_label.config(
            text=f"💰 Maximum Profit: {max_profit}\n🎒 Selected Items: {', '.join(['Item'+str(i+1) for i in selected])}"
        )
        
        # Visualization using Matplotlib
        colors = ['green' if i in selected else 'red' for i in range(len(values))]
        plt.bar(range(1, len(values)+1), values, color=colors)
        plt.title("Knapsack Item Selection")
        plt.xlabel("Item Number")
        plt.ylabel("Value")
        plt.show()
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric inputs!")

# GUI Setup
root = tk.Tk()
root.title("🧠 Knapsack Problem Visualizer")
root.geometry("500x400")
root.config(bg="#1e1e1e")

title = tk.Label(root, text="0/1 Knapsack Problem Visualizer", font=("Helvetica", 16, "bold"), fg="#00ff99", bg="#1e1e1e")
title.pack(pady=15)

tk.Label(root, text="Enter Values (comma-separated):", fg="white", bg="#1e1e1e").pack()
value_entry = tk.Entry(root, width=50)
value_entry.pack(pady=5)

tk.Label(root, text="Enter Weights (comma-separated):", fg="white", bg="#1e1e1e").pack()
weight_entry = tk.Entry(root, width=50)
weight_entry.pack(pady=5)

tk.Label(root, text="Enter Capacity:", fg="white", bg="#1e1e1e").pack()
capacity_entry = tk.Entry(root, width=20)
capacity_entry.pack(pady=5)

btn = tk.Button(root, text="Run Knapsack", command=visualize, bg="#00ff99", fg="black", font=("Helvetica", 12, "bold"))
btn.pack(pady=15)

result_label = tk.Label(root, text="", fg="#ffcc00", bg="#1e1e1e", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()

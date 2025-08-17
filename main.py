# GUI for Process Scheduling Simulator

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import matplotlib.pyplot as plt
# Import scheduling algorithms
from algorithms.FCFS import fcfs 
from algorithms.SJF import sjf
from algorithms.round_robin import round_robin
from algorithms.priority import priority_scheduling
from algorithms.auto import auto_select

# Function to display the result
def display_result(result, selected_algo=None):
    output_text.delete("1.0", tk.END)  # Clear previous output

    if selected_algo:
        output_text.insert(tk.END, f"Auto-Selected Algorithm: {selected_algo}\n\n")

    for p in result['processes']:
        output_text.insert(tk.END, 
            f"Process {p['id']} | Arrival: {p['arrival']} | Burst: {p['burst']} | "
            f"Start: {p['start']} | Completion: {p['completion']} | "
            f"TAT: {p['turnaround']} | WT: {p['waiting']}\n"
        )

    output_text.insert(tk.END, "\n")
    output_text.insert(tk.END, f"Average Waiting Time: {result['average_waiting_time']:.2f}\n")
    output_text.insert(tk.END, f"Average Turnaround Time: {result['average_turnaround_time']:.2f}")

def show_gantt_chart(result):
    fig, gnt = plt.subplots()
    gnt.set_title('Gantt Chart')
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    gnt.set_yticks([15 + 10*i for i in range(len(result['processes']))])
    gnt.set_yticklabels([f"P{p['id']}" for p in result['processes']])
    gnt.set_ylim(0, 10 + 20*len(result['processes']))
    gnt.grid(True)

    for i, p in enumerate(result['processes']):
        start = p['start']
        duration = p['completion'] - p['start']
        gnt.broken_barh([(start, duration)], (10 + 20*i, 9), facecolors='tab:blue')

    plt.show()

# Function to run the selected scheduling algorithm
def run_algorithm():
    selected_algo = algo_var.get()
    process_data = []

    if selected_algo == "Select Algorithm":
        messagebox.showerror("Error", "Please select a scheduling algorithm.")
        return

    # Collect process data from entry fields
    for row in entry_fields:
        pid = row[0].get()
        arrival = row[1].get()
        burst = row[2].get()
        priority = row[3].get()

        if not pid or not arrival or not burst:
            messagebox.showerror("Error", "Please enter PID, Arrival Time, and Burst Time for all processes.")
            return

        try:
            process = {
                "id": int(pid),
                "arrival": int(arrival),
                "burst": int(burst),
            }
            if priority:
                process["priority"] = int(priority)

            process_data.append(process)

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numbers only.")
            return

    result = None

    if selected_algo == "FCFS":
        result = fcfs(process_data)

    elif selected_algo == "SJF":
        result = sjf(process_data)

    elif selected_algo == "Round Robin":
        time_quantum = 2
        result = round_robin(process_data, time_quantum)

    elif selected_algo == "Priority":
        result = priority_scheduling(process_data)

    elif selected_algo == "Auto":
        auto_result = auto_select(process_data)
        selected_algorithm = auto_result['algorithm']
        result = {
            'processes': auto_result['result'],
            'average_waiting_time': auto_result['comparison'][selected_algorithm]['average_waiting_time'],
            'average_turnaround_time': auto_result['comparison'][selected_algorithm]['average_turnaround_time']
        }
        display_result(result, selected_algorithm)
        show_gantt_chart(result)
        return

    if result:
        display_result(result)
        show_gantt_chart(result)

# Main window setup
root = tk.Tk()
root.title("Process Scheduling Simulator")
root.geometry("700x550")

# Dropdown for algorithm selection
algo_var = tk.StringVar()
algo_options = ["Select Algorithm", "Auto", "FCFS", "SJF", "Round Robin", "Priority"]
algo_dropdown = ttk.Combobox(root, textvariable=algo_var, values=algo_options, state="readonly")
algo_dropdown.set("Select Algorithm")
algo_dropdown.pack(pady=10)

# Frame for process input
frame = ttk.Frame(root)
frame.pack(pady=10)

# Table Header
headers = ["PID", "Arrival Time", "Burst Time", "Priority"]
for col, text in enumerate(headers):
    tk.Label(frame, text=text, borderwidth=2, relief="ridge", width=12).grid(row=0, column=col)

# Process Entry Fields (default 5 rows)
entry_fields = []
for i in range(2):
    row = []
    for j in range(4):  # PID, Arrival, Burst, Priority
        entry = ttk.Entry(frame, width=10)
        entry.grid(row=i+1, column=j, padx=5, pady=5)
        row.append(entry)
    entry_fields.append(row)

# Output display
output_text = tk.Text(root, width=80, height=15, state="normal")
output_text.pack(pady=10)

# Run Button
run_button = ttk.Button(root, text="Run Algorithm", command=run_algorithm)
run_button.pack(pady=10)

# Start the GUI loop
root.mainloop()

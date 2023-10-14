import serial
import time
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to update the plot with new temperature values
def update_plot():
    line = serialPort.readline().strip().decode()
    if line:
        temperature_values = line.split()
        if len(temperature_values) == 3:
            try:
                ntc_temp = float(temperature_values[0])
                lm35_temp = float(temperature_values[1])
                ds18b20_temp = float(temperature_values[2])
                
                # Update the label text with new temperature values
                temp_label.config(text=f"NTC: {ntc_temp:.2f}\nLM35: {lm35_temp:.2f}\nDS18B20: {ds18b20_temp:.2f}")
                
                # Update the table
                tree.insert('', 'end', values=(ntc_temp, lm35_temp, ds18b20_temp))
                
                # Update the plot
                x_data.append(time.time())
                y_data_ntc.append(ntc_temp)
                y_data_lm35.append(lm35_temp)
                y_data_ds18b20.append(ds18b20_temp)
                line_ntc.set_data(x_data, y_data_ntc)
                line_lm35.set_data(x_data, y_data_lm35)
                line_ds18b20.set_data(x_data, y_data_ds18b20)
                
                # Auto-adjust the plot's x-axis
                ax.relim()
                ax.autoscale_view()
                
                # Redraw the canvas
                canvas.draw()
                
            except ValueError:
                print("Error: Unable to convert temperature values to floats.")
        else:
            print("Error: Invalid number of temperature values in the line.")
    
    root.after(1000, update_plot)  # Schedule the update function to run every 1 second

# Create the main application window
root = tk.Tk()
root.title("Real-time Temperature Monitor")

# Create a label for displaying the temperature values
temp_label = ttk.Label(root, text="NTC: N/A\nLM35: N/A\nDS18B20: N/A")
temp_label.pack()

# Create a Matplotlib figure and subplot for the real-time plot
fig, ax = plt.subplots()
x_data, y_data_ntc, y_data_lm35, y_data_ds18b20 = [], [], [], []
line_ntc, = ax.plot(x_data, y_data_ntc, label='NTC')
line_lm35, = ax.plot(x_data, y_data_lm35, label='LM35')
line_ds18b20, = ax.plot(x_data, y_data_ds18b20, label='DS18B20')
ax.set_xlabel('Time')
ax.set_ylabel('Temperature')
ax.legend()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Create a table to display the temperature values
tree = ttk.Treeview(root, columns=("NTC", "LM35", "DS18B20"))
tree.heading('#1', text='NTC')
tree.heading('#2', text='LM35')
tree.heading('#3', text='DS18B20')
tree.pack()

# Insert initial columns
tree.insert('', 'end', values=(0.0, 0.0, 0.0))

# Define the serial port
serialPort = serial.Serial('COM3', baudrate=115200, timeout=1)
time.sleep(2)

# Start updating the plot and table
update_plot()

# Start the tkinter main loop
root.mainloop()

# Close the serial port when the GUI is closed
serialPort.close()
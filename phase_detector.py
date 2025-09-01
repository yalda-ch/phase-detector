import tkinter as tk
from tkinter import messagebox
import pandas as pd
temperature_data = pd.DataFrame({
    'Temperature': [0.01, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 374.1],
    'Pressure': [0.6113, 0.8721, 1.2276, 1.705, 2.339, 3.169, 4.246, 5.628, 7.384, 9.593, 12.35, 15.758, 19.941, 25.03, 31.19, 38.58, 47.39, 57.83, 70.14, 84.55, 101.3, 120.8, 143.3, 169.1, 198.5, 232.1, 270.1, 313.0, 361.3, 415.4, 475.9, 543.1, 617.8, 700.5, 791.7, 892.0, 1002.2, 1122.7, 1254.4, 1397.8, 1553.8, 1723.0, 1906.3, 2104.2, 2317.8, 2547.7, 2794.9, 3060.1, 3344.2, 3648.2, 3973.0, 4319.5, 4688.6, 5081.3, 5498.7, 5941.8, 6411.7, 6909.4, 7436.0, 7992.8, 8581.0, 9201.8, 9856.6, 10547.0, 11274.0, 12040.0, 12845.0, 13694.0, 14586.0, 15525.0, 16514.0, 17554.0, 18651.0, 19807.0, 21028.0, 22089.0]
})
pressure_data = pd.DataFrame({
    'Pressure': [0.6113, 0.8721, 1.2276, 1.705, 2.339, 3.169, 4.246, 5.628, 7.384, 9.593, 12.35, 15.758, 19.941, 25.03, 31.19, 38.58, 47.39, 57.83, 70.14, 84.55, 101.3, 120.8, 143.3, 169.1, 198.5, 232.1, 270.1, 313.0, 361.3, 415.4, 475.9, 543.1, 617.8, 700.5, 791.7, 892.0, 1002.2, 1122.7, 1254.4, 1397.8, 1553.8, 1723.0, 1906.3, 2104.2, 2317.8, 2547.7, 2794.9, 3060.1, 3344.2, 3648.2, 3973.0, 4319.5, 4688.6, 5081.3, 5498.7, 5941.8, 6411.7, 6909.4, 7436.0, 7992.8, 8581.0, 9201.8, 9856.6, 10547.0, 11274.0, 12040.0, 12845.0, 13694.0, 14586.0, 15525.0, 16514.0, 17554.0, 18651.0, 19807.0, 21028.0, 22089.0],
    'Temperature': [0.01, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 374.1]
})
def check_phase():
    try:
        temperature = float(temp_entry.get())
        pressure = float(press_entry.get())
        compare_type = compare_var.get()
        if compare_type == "temperature":
            sat_data = temperature_data[temperature_data['Temperature'] == temperature]
            if not sat_data.empty:
                sat_pressure = sat_data['Pressure'].iloc[0]
                if pressure > sat_pressure:
                    phase = "Compressed liquid"
                elif pressure < sat_pressure:
                    phase = "Superheated vapor"
                else:
                    phase = "Two-phase mixture"
            else:
                phase = "Temperature out of range of the table."
        elif compare_type == "pressure":
            sat_data = pressure_data[pressure_data['Pressure'] == pressure]
            if not sat_data.empty:
                sat_temperature = sat_data['Temperature'].iloc[0]
                if temperature < sat_temperature:
                    phase = "Compressed liquid"
                elif temperature > sat_temperature:
                    phase = "Superheated vapor"
                else:
                    phase = "Two-phase mixture"
            else:
                phase = "Pressure out of range of the table."
        else:
            phase = "Invalid comparison type."
        
        messagebox.showinfo("Result", f"Phase: {phase}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Phase Detector")
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_text(250, 20, text="Phase Detector", fill="darkblue", font=("Arial", 20, "bold"))
canvas.create_text(120, 70, text="Temperature (°C) :", fill="blue")
temp_entry = tk.Entry(root)
canvas.create_window(280, 70, window=temp_entry)
canvas.create_text(120, 110, text="Pressure (KPa) :", fill="blue")
press_entry = tk.Entry(root)
canvas.create_window(280, 110, window=press_entry)
canvas.create_text(120, 150, text="Comparison Type :", fill="magenta")
compare_var = tk.StringVar(value="temperature")
radio_temp = tk.Radiobutton(root, text="Temperature", variable=compare_var, value="temperature")
canvas.create_window(280, 150, window=radio_temp)
radio_press = tk.Radiobutton(root, text="Pressure", variable=compare_var, value="pressure")
canvas.create_window(280, 180, window=radio_press)
check_button = tk.Button(root, text="Check Phase", command=check_phase, fg="red")
canvas.create_window(250, 230, window=check_button)
root.mainloop()
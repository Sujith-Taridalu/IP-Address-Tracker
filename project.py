import tkinter as tk
import requests
import webbrowser


def track_ip():
    ip_address = ip_entry.get()
    api_key = "5e211562d3cd4d0b836a946780c08148"
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
    response = requests.get(url)
    data = response.json()
    country_label.config(text=data['country_name'])
    state_label.config(text=data['state_prov'])
    city_label.config(text=data['city'])
    isp_label.config(text=data['isp'])
    latitude = data["latitude"]
    longitude = data["longitude"]
    map_button.config(state=tk.NORMAL, command=lambda: open_google_maps(latitude, longitude))


def open_google_maps(latitude, longitude):
    url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
    webbrowser.open_new_tab(url)


root = tk.Tk()
root.title("IP Address Tracker")
root.configure(bg="#f0f0f0")  # Set background color

# Create and configure a frame for the input section
input_frame = tk.Frame(root, bg="#f0f0f0")  # Set background color
input_frame.pack(pady=10)

ip_label = tk.Label(input_frame, text="Enter IP Address:", bg="#f0f0f0")  # Set background color
ip_label.grid(row=0, column=0)

ip_entry = tk.Entry(input_frame, width=30)
ip_entry.grid(row=0, column=1)

track_button = tk.Button(input_frame, text="Track IP", command=track_ip, bg="#4caf50", fg="white")
# Set background and foreground color

track_button.grid(row=0, column=2, padx=10)

# Create and configure a frame for the results section
results_frame = tk.Frame(root, bg="#f0f0f0")  # Set background color
results_frame.pack(pady=10)

result_label = tk.Label(results_frame, text="Results:", bg="#f0f0f0")  # Set background color
result_label.grid(row=0, column=0, sticky="w")

country_label = tk.Label(results_frame, text="", bg="#f0f0f0")  # Set background color
country_label.grid(row=1, column=0, sticky="w")

state_label = tk.Label(results_frame, text="", bg="#f0f0f0")  # Set background color
state_label.grid(row=2, column=0, sticky="w")

city_label = tk.Label(results_frame, text="", bg="#f0f0f0")  # Set background color
city_label.grid(row=3, column=0, sticky="w")

isp_label = tk.Label(results_frame, text="", bg="#f0f0f0")  # Set background color
isp_label.grid(row=4, column=0, sticky="w")

# Create and configure a frame for the map button
map_frame = tk.Frame(root, bg="#f0f0f0")  # Set background color
map_frame.pack(pady=10)

map_button = tk.Button(map_frame, text="Open in Google Maps", state=tk.DISABLED, bg="#2196f3", fg="white")
# Set background and foreground color

map_button.pack()

root.mainloop()

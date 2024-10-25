from tkinter import *
from tkinter import messagebox as mb
from datetime import datetime
import requests
from PIL import Image, ImageTk  # Pillow for image display
import io

# Function to fetch weather data
def get_weather():
    global city
    city = city_input.get()  # Get the city name from the input field
    api_key = "01cd144c08b04e57d27e335f4ca8d65d"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Send a request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract weather details
        temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        min_temp = data['main']['temp_min'] - 273.15  # Min temp
        max_temp = data['main']['temp_max'] - 273.15  # Max temp
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed'] * 3.6  # Convert from m/s to km/h
        epoch_time = data['dt']
        date_time = datetime.fromtimestamp(epoch_time)
        desc = data['weather'][0]['description']
        cloudy = data['clouds']['all']
        icon_code = data['weather'][0]['icon']  # Get weather icon code

        # Update the labels with fetched data
        timelabel.config(text="Updated: " + str(date_time))
        temp_field.config(text=f'{temp:.2f} °C')
        min_temp_field.config(text=f'{min_temp:.2f} °C')
        max_temp_field.config(text=f'{max_temp:.2f} °C')
        pressure_field.config(text=f'{pressure} hPa')
        humid_field.config(text=f'{humidity} %')
        wind_field.config(text=f'{wind:.2f} km/h')
        cloud_field.config(text=f'{cloudy} %')
        desc_field.config(text=str(desc).capitalize())

        # Fetch and display the weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        img_data = icon_response.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((100, 100))  # Resize to fit the UI
        img_tk = ImageTk.PhotoImage(img)
        icon_label.config(image=img_tk)
        icon_label.image = img_tk  # Keep a reference to avoid garbage collection

    else:
        mb.showerror("Error", "City Not Found. Enter a valid city name.")
        city_input.delete(0, END)

# Function to reset all fields
def reset():
    city_input.delete(0, END)
    temp_field.config(text="")
    min_temp_field.config(text="")
    max_temp_field.config(text="")
    pressure_field.config(text="")
    humid_field.config(text="")
    wind_field.config(text="")
    cloud_field.config(text="")
    desc_field.config(text="")
    timelabel.config(text="")
    icon_label.config(image="")

# Create the main application window
root = Tk()
root.title('Weather Application')
root.configure(bg='#2a9d8f')
root.geometry("550x650")

# Title label
title = Label(root, text='Weather Detection', fg='white', bg='#2a9d8f', font=('Helvetica', 22, 'bold'))
title.grid(row=0, column=0, columnspan=2, pady=20)

# Input field and labels
label1 = Label(root, text='Enter the City Name:', font=('Helvetica', 12), bg='#2a9d8f', fg='white')
city_input = Entry(root, width=20, font=('Helvetica', 14), relief=GROOVE)
label1.grid(row=1, column=0, padx=10, pady=10, sticky='W')
city_input.grid(row=1, column=1, padx=10, pady=10)

# Buttons
btn_submit = Button(root, text='Get Weather', width=14, font=('Helvetica', 12), bg='#0077b6', fg='white', command=get_weather)
btn_submit.grid(row=2, column=1, padx=10, pady=10)

# Weather icon
icon_label = Label(root, bg='#2a9d8f')
icon_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Weather fields
temp_label = Label(root, text="Temperature:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
min_temp_label = Label(root, text="Min Temp:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
max_temp_label = Label(root, text="Max Temp:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
pressure_label = Label(root, text="Pressure:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
humidity_label = Label(root, text="Humidity:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
wind_label = Label(root, text="Wind:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
cloud_label = Label(root, text="Cloudiness:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
desc_label = Label(root, text="Description:", font=('Helvetica', 12), bg='#2a9d8f', fg='white')

temp_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
min_temp_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
max_temp_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
pressure_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
humid_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
wind_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
cloud_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')
desc_field = Label(root, text="", font=('Helvetica', 12), bg='#2a9d8f', fg='white')

temp_label.grid(row=4, column=0, padx=10, pady=5, sticky='W')
temp_field.grid(row=4, column=1, padx=10, pady=5, sticky='W')
min_temp_label.grid(row=5, column=0, padx=10, pady=5, sticky='W')
min_temp_field.grid(row=5, column=1, padx=10, pady=5, sticky='W')
max_temp_label.grid(row=6, column=0, padx=10, pady=5, sticky='W')
max_temp_field.grid(row=6, column=1, padx=10, pady=5, sticky='W')
pressure_label.grid(row=7, column=0, padx=10, pady=5, sticky='W')
pressure_field.grid(row=7, column=1, padx=10, pady=5, sticky='W')
humidity_label.grid(row=8, column=0, padx=10, pady=5, sticky='W')
humid_field.grid(row=8, column=1, padx=10, pady=5, sticky='W')
wind_label.grid(row=9, column=0, padx=10, pady=5, sticky='W')
wind_field.grid(row=9, column=1, padx=10, pady=5, sticky='W')
cloud_label.grid(row=10, column=0, padx=10, pady=5, sticky='W')
cloud_field.grid(row=10, column=1, padx=10, pady=5, sticky='W')
desc_label.grid(row=11, column=0, padx=10, pady=5, sticky='W')
desc_field.grid(row=11, column=1, padx=10, pady=5, sticky='W')

# Time label
timelabel = Label(root, text='', bg='#2a9d8f', font=('Helvetica', 14), fg='white')
timelabel.grid(row=12, column=0, columnspan=2, padx=10, pady=20)

# Reset button
btn_reset = Button(root, text='Reset', font=('Helvetica', 12), bg='#e63946', fg='white', command=reset)
btn_reset.grid(row=13, column=1, padx=10, pady=10)

# Run the application
root.mainloop()

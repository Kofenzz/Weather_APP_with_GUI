from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}"

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        #(City, Country, Temperature_celsius,icon,weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = temp_celsius * 9 / 5 +32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        print(final)
        return final
        
    else:
        return None
    
def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = f'{weather[0]}, {weather[1]}'
        # image['bitmap'] = 'weather_icon\\{}.png'.format(weather[4])
        img["file"] = 'weather_icons\\{}.png'.format(weather[4])
        temp_lbl['text'] = f'{weather[2]:.2f}°C, {weather[3]:.2f}°F'
        weather_lbl["text"] = f'{weather[5]}'
    else:
        messagebox.showerror("Error", "Cannot find city {}".format(city))


app = Tk()
app.title("Weather application")
app.geometry("700x350")
app.configure(bg="grey")


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search Weather",width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text="", font=('bold', 20), bg='grey')
location_lbl.pack()

img = PhotoImage(file= "")
Image = Label(app, image = img, bg='grey')
Image.pack()

# image = Label(app, bitmap='')
# image.pack()

temp_lbl = Label(app, text='', bg='grey', font=('bold'))
temp_lbl.pack()

weather_lbl = Label(app, text='', bg='grey', font=('bold'))
weather_lbl.pack()




app.mainloop()
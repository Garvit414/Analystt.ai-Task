import requests
import time

def get_weather_info(city):
    api_key = "eea37893e6d01d234eca31616e48c631"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        w_data = response.json()

        weather = w_data['weather'][0]['main']
        temp = int(w_data['main']['temp'] - 273.15)
        temp_min = int(w_data['main']['temp_min'] - 273.15)
        temp_max = int(w_data['main']['temp_max'] - 273.15)
        pressure = w_data['main']['pressure']
        humidity = w_data['main']['humidity']
        visibility = w_data['visibility']
        wind = w_data['wind']['speed']
        sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
        sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

        all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
        all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                    f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                    f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                    f"\nSunset: {sunset}"

        return all_data1, all_data2

    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}", None
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}", None
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}", None
    except requests.exceptions.RequestException as err:
        return f"An error occurred: {err}", None

def main():
    speak("Tell me the city name.")
    city = takeCommand().lower()

    weather_data = get_weather_info(city)

    if weather_data[0] is not None:
        speak(f"Gathering the weather information of {city}...")
        print(f"Gathering the weather information of {city}...")
        print(weather_data[0])
        speak(weather_data[0])

        if weather_data[1] is not None:
            print(weather_data[1])
            speak(weather_data[1])
    else:
        print(f"Failed to retrieve weather information for {city}. Please check the city name.")

if __name__ == "__main__":
    main()

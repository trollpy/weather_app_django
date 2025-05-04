# ☁️ Django Weather App

![Weather App Banner](/weatherproject/image.png)

## 🌈 Overview

Django Weather App is an enchanting weather application that brings weather forecasting to life with a dynamic, animated interface. Built with Django and the OpenWeatherMap API, this app transforms ordinary weather checking into an immersive experience with a sky that changes colors throughout the day and drifting animated clouds.

## ✨ Features

- **Stunning Animated UI**: Sky background that transitions through day, sunset, night, and sunrise colors
- **Dynamic Cloud Animations**: Realistic cloud movements that create an immersive atmosphere
- **Real-time Weather Data**: Accurate current conditions for any city worldwide
- **Interactive Cards**: Elegantly designed weather cards with hover effects
- **5-Day Forecast**: Plan ahead with the extended weather forecast
- **Responsive Design**: Beautiful experience on any device size
- **Search History**: Easily access your recently viewed locations
- **Modern Visual Effects**: Subtle shadows, transitions, and card interactions

## 🎭 Visual Experience

- **Animated Sky**: Background gradient that cycles through time-of-day colors
- **Moving Clouds**: Dynamically generated cloud elements that drift across the screen
- **Interactive Elements**: Cards that respond to user interaction with subtle animations
- **Glass-morphism Design**: Semi-transparent cards with backdrop blur for a modern look
- **Weather Icons**: Visual representation of current weather conditions

## 🛠️ Technologies

- **Backend**: Python 3.x, Django 5.x
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **API**: OpenWeatherMap API
- **Animation**: CSS Keyframes and JavaScript DOM manipulation
- **Data Storage**: SQLite (default Django database)

## 📋 Prerequisites

- Python 3.8 or higher
- Django 5.x
- Free OpenWeatherMap API key

## ⚙️ Installation

### 1. Clone or download this repository
```bash
git clone https://your-repository-url/django-weather-app.git
cd django-weather-app
```

### 2. Create and activate a virtual environment
```bash
# Create virtual environment
python -m venv weatherenv

# Activate virtual environment
# On Windows:
weatherenv\Scripts\activate
# On macOS/Linux:
source weatherenv/bin/activate
```

### 3. Install required packages
```bash
pip install django requests
```

### 4. Configure your OpenWeatherMap API key
Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)

Open `weatherproject/settings.py` and add your API key:
```python
# Weather API settings
OPENWEATHERMAP_API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
```

### 5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server
```bash
python manage.py runserver
```

### 7. Access the application
Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📱 Usage

1. Enter a city name in the search box
2. Click "Get Weather" or press Enter
3. View the current weather information with beautiful visual representation
4. Explore the 5-day forecast (requires additional implementation in views.py)
5. Watch the animated sky and clouds as you check different locations
6. Review your search history at the bottom of the page

## 🌟 UI Features Explained

### Dynamic Sky Background
The app features a gradient background that transitions through:
- Light blue (day)
- Orange/yellow (sunset) 
- Purple/dark blue (night)
- Pink/orange (sunrise)

### Cloud Animation System
- Multiple cloud layers moving at different speeds
- Dynamically generated clouds with randomized properties
- Custom CSS shapes to create realistic cloud formations

### Weather Cards
- Glass-morphism design with backdrop filter blur
- Hover effects that elevate cards and enhance shadows
- Smooth transitions between states

## 📸 Screenshots

![Weather App Home](https://via.placeholder.com/600x300?text=Weather+App+Home+Screen)
*Home screen with animated sky and search functionality*

![Weather Information](https://via.placeholder.com/600x300?text=Weather+Information+Display)
*Weather information display with animated background*

![Forecast View](https://via.placeholder.com/600x300?text=5-Day+Forecast+Display)
*5-day forecast with interactive cards*

## 🚀 Enabling the Forecast Feature

To enable the 5-day forecast feature that's included in the UI, you'll need to modify your Django views to fetch forecast data. Add this to your `views.py`:

```python
def index(request):
    # Existing view code...
    
    # For forecast data
    forecast_data = None
    if weather_data:
        # Get city coordinates from weather_data
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']
        
        # Call OpenWeatherMap 5-day forecast API
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={settings.OPENWEATHERMAP_API_KEY}'
        
        try:
            forecast_response = requests.get(forecast_url)
            forecast_response.raise_for_status()
            forecast_json = forecast_response.json()
            
            # Process forecast data (one entry per day)
            forecast_data = []
            added_dates = set()
            
            for item in forecast_json['list']:
                date = item['dt_txt'].split(' ')[0]
                
                # Only add one forecast per day
                if date not in added_dates:
                    forecast_data.append({
                        'date': datetime.strptime(date, '%Y-%m-%d').strftime('%a'),  # Day name
                        'temp': round(item['main']['temp']),
                        'icon': item['weather'][0]['icon'],
                        'description': item['weather'][0]['description']
                    })
                    added_dates.add(date)
                
                # Stop after 5 days
                if len(forecast_data) >= 5:
                    break
        except:
            forecast_data = None
    
    context = {
        'form': form,
        'weather_data': weather_data,
        'forecast_data': forecast_data,  # Add to context
        'error_message': error_message,
        'recent_searches': recent_searches
    }
    
    # Don't forget to add this import at the top:
    # from datetime import datetime
```

## 📝 Customization Options

### Changing the Sky Animation
You can modify the sky gradient colors in the CSS by editing the `@keyframes sky-color-change` section:

```css
@keyframes sky-color-change {
    0% { background: linear-gradient(to bottom, #87CEEB, #B0E0E6); } /* Day */
    25% { background: linear-gradient(to bottom, #FFA07A, #FFD700); } /* Sunset */
    50% { background: linear-gradient(to bottom, #4B0082, #000080); } /* Night */
    75% { background: linear-gradient(to bottom, #FF69B4, #FFA07A); } /* Sunrise */
    100% { background: linear-gradient(to bottom, #87CEEB, #B0E0E6); } /* Back to day */
}
```

### Adding More Cloud Elements
You can generate additional clouds by modifying the JavaScript function:

```javascript
// Increase the number of clouds
for (let i = 0; i < 6; i++) {  // Change from 3 to 6
    createCloud(i);
}
```

## 🔮 Future Enhancements

- **Weather-Based Backgrounds**: Dynamic backgrounds that match the current weather conditions
- **Animated Weather Icons**: Add movement to weather icons based on conditions
- **Sound Effects**: Optional ambient sounds matching the weather (rain, thunder, etc.)
- **User Accounts**: Save favorite cities and personalize the experience
- **Weather Alerts**: Notifications for severe weather conditions
- **Show weather forecast too** 
- **Multiple Cities**: Compare weather between different locations
- **Historical Data**: View and graph past weather patterns
- **Weather Maps**: Interactive radar and satellite imagery

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💬 Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Animation techniques inspired by modern web design trends
- Cloud animation design based on CSS-Tricks tutorials

---

<p align="center">
  Made with ❤️ and ☁️
</p>

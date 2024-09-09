import os
import redis
import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Load environment variables
API_KEY = os.getenv("VISUAL_CROSSING_API_KEY")
REDIS_URL = os.getenv("redis://localhost:6379")

# Connect to Redis
r = redis.Redis.from_url(REDIS_URL)

@app.route("/weather/<city>")
def get_weather(city):
    # Check if weather data is in Redis cache
    cache_key = f"weather_{city}"
    weather_data = r.get(cache_key)
    if weather_data:
        return jsonify(json.loads(weather_data))

    # Fetch weather data from Visual Crossing API
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        # Store weather data in Redis cache with 12-hour expiration
        r.set(cache_key, json.dumps(weather_data), ex=43200)
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Failed to fetch weather data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
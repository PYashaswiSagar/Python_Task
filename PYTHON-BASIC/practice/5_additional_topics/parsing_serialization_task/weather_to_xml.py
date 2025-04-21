import os
import json
from statistics import mean
from lxml import etree

DATA_DIR = './list_of_cities'  # This folder should contain 17 folders for cities

def process_city_data(city_path):
    """Parse a city's JSON weather data and compute required statistics."""
    json_files = [f for f in os.listdir(city_path) if f.endswith('.json')]
    if not json_files:
        raise ValueError(f"No JSON file found in {city_path}")
    filename = json_files[0]

    with open(os.path.join(city_path, filename), 'r', encoding='utf-8', errors='replace') as f:
        data = json.load(f)
    
    temps = [hour['temp'] for hour in data['hourly']]
    winds = [hour['wind_speed'] for hour in data['hourly']]

    return {
        'mean_temp': round(mean(temps), 2),
        'min_temp': round(min(temps), 2),
        'max_temp': round(max(temps), 2),
        'mean_wind_speed': round(mean(winds), 2),
        'min_wind_speed': round(min(winds), 2),
        'max_wind_speed': round(max(winds), 2),
    }

def build_xml(weather_data, date="2021-09-25", country="Spain"):
    """Build the output XML tree using lxml."""
    root = etree.Element("weather", country=country, date=date)
    
    # Get summary stats
    all_mean_temps = {city: data['mean_temp'] for city, data in weather_data.items()}
    all_mean_winds = {city: data['mean_wind_speed'] for city, data in weather_data.items()}

    summary = etree.SubElement(root, "summary",
        mean_temp=str(round(mean(all_mean_temps.values()), 2)),
        mean_wind_speed=str(round(mean(all_mean_winds.values()), 2)),
        coldest_place=min(all_mean_temps, key=all_mean_temps.get),
        warmest_place=max(all_mean_temps, key=all_mean_temps.get),
        windiest_place=max(all_mean_winds, key=all_mean_winds.get),
    )

    # Add cities
    cities_el = etree.SubElement(root, "cities")
    for city, stats in weather_data.items():
        etree.SubElement(cities_el, city.replace(" ", "_"),  # Avoid XML tag issues
            mean_temp=str(stats['mean_temp']),
            max_temp=str(stats['max_temp']),
            min_temp=str(stats['min_temp']),
            mean_wind_speed=str(stats['mean_wind_speed']),
            max_wind_speed=str(stats['max_wind_speed']),
            min_wind_speed=str(stats['min_wind_speed']),
        )

    return root

def main():
    weather_data = {}
    for city_folder in os.listdir(DATA_DIR):
        city_path = os.path.join(DATA_DIR, city_folder)
        if os.path.isdir(city_path):
            stats = process_city_data(city_path)
            weather_data[city_folder] = stats

    xml_tree = build_xml(weather_data)
    
    # Save XML
    with open("spain_weather_2021-09-25.xml", 'wb') as f:
        f.write(etree.tostring(xml_tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

    print(f"XML written to {"spain_weather_2021-09-25.xml"}")

if __name__ == "__main__":
    main()


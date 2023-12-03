import os
import re
from collections import Counter
from Temperature_Substrate import extract_temperature

def convert_to_K(match):
    temperature_str = match.group()
    if '°C' in temperature_str:
        temperature = float(temperature_str.replace('°C', '')) + 273.15
    elif 'K' in temperature_str:
        temperature = float(temperature_str.replace('K', ''))
    else:
        print(f"No match found: {temperature_str}")
        return temperature_str
    return f"{temperature} K"

data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]
total_frequencies = Counter()

for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:
        paragraph = file.read()
        temperature_pattern = r"\b\d+\.\d+\s*(?:°C|K)\b"
        paragraph = re.sub(temperature_pattern, convert_to_K, paragraph)
        result = extract_temperature(paragraph)
        temperature_frequencies = Counter(result)
        total_frequencies += temperature_frequencies

converted_sorted_words = []
for temperature, frequency in total_frequencies.items():
    if '°C' in temperature:
        temperature_value = float(temperature.replace('°C', '')) + 273.15
        converted_temperature = f"{temperature_value} K"
        converted_sorted_words.append((converted_temperature, frequency))
    else:
        converted_sorted_words.append((temperature, frequency))

def process_data_tem(sorted_data, interval=100):
    result = Counter()
    for temperature, frequency in sorted_data:
        temperature_value = None
        try:
            try:
                temperature_value = float(temperature.replace(' K', ''))
            except ValueError:
                temperature_value = float(temperature.replace('K', ''))
        except ValueError:
            pass
        if temperature_value is not None:
            temperature_range = int(temperature_value / interval) * interval
            result[temperature_range] += frequency
    sorted_result = sorted(result.items(), key=lambda x: x[0])
    temperature_ranges = [f"{temperature_range}-{temperature_range + interval} K" for temperature_range, _ in sorted_result]
    frequencies = [frequency for _, frequency in sorted_result]
    return temperature_ranges, frequencies

interval = 100
temperature_ranges, frequencies = process_data_tem(converted_sorted_words, interval)

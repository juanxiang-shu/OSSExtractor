import os
import re
from collections import Counter
from Compounds import find_words

def convert_to_K(match):
    temperature, unit = match.groups()
    temperature = float(temperature)
    if unit == '°C':
        temperature += 273.15
    return temperature

data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt') and os.path.isfile(f)]

total_frequencies = Counter()

for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:
        paragraph = file.read()

        temperature_pattern = r'(\d+(?:\.\d+)?)\s*(°C|K)'

        paragraph = re.sub(temperature_pattern, convert_to_K, paragraph)

        result = find_words(paragraph)
        if "temperature" in result:
            substrate_frequencies = Counter(result["temperature"])

            total_frequencies += substrate_frequencies

temperature_ranges = [i for i in range(0, 1301, 100)]

temperature_frequency_ranges = [0.0] * len(temperature_ranges)

for temperature, frequency in total_frequencies.items():
    temperature = float(temperature)
    for i, temp_range in enumerate(temperature_ranges):
        if temp_range <= temperature < temp_range + 100:
            temperature_frequency_ranges[i] += frequency
            break

print("Temperature Frequencies Range:")
for i, temp_range in enumerate(temperature_ranges):
    print(f"{temp_range} K - {temp_range+100} K: {temperature_frequency_ranges[i]}")

import re
from collections import Counter
from Compounds import find_words


def extract_temperature(paragraph):
    temperature_filter = set()
    sentences = paragraph.split(".")
    temperature_count = Counter()
    pattern = r'\b(annealing|postannealing|post annealing|annealed|activated|prepared|evaporated)\b'
    prefix_pattern = re.compile(r'^(400K|378 K| 570 K|170 K|700 K|127 °C|400 °C|850 K|500 °C|873 K|239 K|225 K|'
                                r'675 K|745 K|593 K|433 K|393 K|473 K|513 K|553 K|373 K|773 K|130 K|490 K|240 K|230 °C|'
                                r'570 K|190 °C|275 °C|205 °C|740 K|650 K|780 K|315 K|370 K|380 °C|530 °C|150 °C|470 °C|180 K|'
                                r'660 K|630 K|300 °C|770 K|750 K|500 K|320 K|800 K|220 K|330 K|170 °C)')

    for sentence in sentences:
        sentence = sentence.strip()
        if re.search(pattern, sentence, re.IGNORECASE):
            result = find_words(sentence)
            for temp_str in result["temperature"]:
                try:
                    if "K" in temp_str:
                        temp_value = int(re.search(r'\d+', temp_str).group())
                        if 121 <= temp_value <= 999:
                            temperature_filter.add(temp_str)
                            temperature_count[temp_str] += 1
                    elif "°C" in temp_str:
                        temp_value = int(re.search(r'\d+', temp_str).group())
                        if 99 <= temp_value <= 599:
                            temperature_filter.add(temp_str)
                            temperature_count[temp_str] += 1
                except ValueError:
                    pass

    filtered_temperature = {temp for temp, count in temperature_count.items() if count >= 1}
    temperature_to_remove = [compound for compound in filtered_temperature if re.match(prefix_pattern, compound)]

    for temp in temperature_to_remove:
        filtered_temperature.remove(temp)
    return filtered_temperature
# def extract_temperature(paragraph):
#     temperature_filter = set()
#     sentences = paragraph.split(".")
#     temperature_count = Counter()
#     pattern = r'\b(annealing|postannealing|post annealing|annealed|activated|prepared|evaporated)\b'  #decorated|deposition|Deposition|adsorbed|
#     for sentence in sentences:
#         sentence = sentence.strip()
#         if re.search(pattern, sentence, re.IGNORECASE):
#             result = find_words(sentence)
#             temperature_filter |= set(result["temperature"])
#             temperature_count.update(result["temperature"])
#     filtered_temperature = {temp for temp, count in temperature_count.items() if count >= 1}
#     return filtered_temperature

def extract_substrate(paragraph):
    substrate_filter = set()
    sentences = paragraph.split(".")
    pattern = r'\b(decorated|deposited|deposition|Deposition|adsorbed|annealing|postannealing|post annealing)\b'
    exclusion_pattern = re.compile(r'Si\(111\)|Pb\(111\)|Rh\(111\)')

    for sentence in sentences:
        sentence = sentence.strip()
        if re.search(pattern, sentence, re.IGNORECASE):
            result = find_words(sentence)
            substrate_filter |= set(result["substrate"])

    substrate_filter = {compound for compound in substrate_filter if not re.search(exclusion_pattern, compound)}

    return substrate_filter
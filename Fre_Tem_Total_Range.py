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

# 获取所有数据文件的路径，并过滤出符合条件的文件
data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt') and os.path.isfile(f)]

# 创建一个空的词频统计字典
total_frequencies = Counter()

# 遍历每个数据文件
for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:
        paragraph = file.read()

        # 温度数据转换函数的正则表达式模式
        temperature_pattern = r'(\d+(?:\.\d+)?)\s*(°C|K)'

        # 将paragraph中的温度数据转换为K形式
        paragraph = re.sub(temperature_pattern, convert_to_K, paragraph)

        # 调用find_words函数获取词频信息
        result = find_words(paragraph)
        if "temperature" in result:
            substrate_frequencies = Counter(result["temperature"])

            # 将当前文章的词频信息累加到总词频字典中
            total_frequencies += substrate_frequencies

# 定义温度区间
temperature_ranges = [i for i in range(0, 1301, 100)]

# 创建一个列表，用于存储每个温度区间内的频率
temperature_frequency_ranges = [0.0] * len(temperature_ranges)

# 统计每个温度区间内的频率
for temperature, frequency in total_frequencies.items():
    temperature = float(temperature)  # Convert temperature to float
    for i, temp_range in enumerate(temperature_ranges):
        if temp_range <= temperature < temp_range + 100:
            temperature_frequency_ranges[i] += frequency
            break

# 输出按温度区间统计后的词频信息
print("Temperature Frequencies Range:")
for i, temp_range in enumerate(temperature_ranges):
    print(f"{temp_range} K - {temp_range+100} K: {temperature_frequency_ranges[i]}")

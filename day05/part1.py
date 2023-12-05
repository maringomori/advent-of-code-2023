
import math
#Find the location of a string and the text after it until empty line
def find_string_location_and_text_before_empty_line(input, string):
    output = []
    for i, line in enumerate(input):
        if string in line:
            for j, line2 in enumerate(input[i+1:]):
                if line2.strip() == "":
                    return output
                output.append(input[i+j+1].strip())
                

def map_n_to_m(n_to_m):
    source_target_sets = []

    for i in n_to_m:
        nums = i.strip().split(" ")
        dest_start = int(nums[0])
        source_start = int(nums[1])
        dest_end = int(nums[0]) + (int(nums[2])) - 1
        source_end = int(nums[1]) + (int(nums[2])) - 1
        source_target_sets.append((source_start, source_end, dest_start, dest_end))
    return source_target_sets



# Find source if its between the source_target_sets values
def find_source(source_target_sets, source):
    print(source_target_sets)
    for i in source_target_sets:
        if i[0] <= source <= i[1]:
            return i[2] + source - i[0]
    return source

input = open("input.txt", "r").readlines()

seeds = input[0].split(":")[1].strip().split(" ")

print(seeds)


seed_to_soils = find_string_location_and_text_before_empty_line(input, "seed-to-soil map:")
soil_to_fertilizer = find_string_location_and_text_before_empty_line(input, "soil-to-fertilizer map:")
fertilizer_to_water = find_string_location_and_text_before_empty_line(input, "fertilizer-to-water map:")
water_to_light = find_string_location_and_text_before_empty_line(input, "water-to-light map:")
light_to_temperature = find_string_location_and_text_before_empty_line(input, "light-to-temperature map:")
temperature_to_humidity = find_string_location_and_text_before_empty_line(input, "temperature-to-humidity map:")
humidity_to_location = find_string_location_and_text_before_empty_line(input, "humidity-to-location map:")

seed_to_soils_sets = map_n_to_m(seed_to_soils)
soil_to_fertilizer_sets = map_n_to_m(soil_to_fertilizer)
fertilizer_to_water_sets = map_n_to_m(fertilizer_to_water)
water_to_light_sets = map_n_to_m(water_to_light)
light_to_temperature_sets = map_n_to_m(light_to_temperature)
temperature_to_humidity_sets = map_n_to_m(temperature_to_humidity)
humidity_to_location_sets = map_n_to_m(humidity_to_location)

min_location = math.inf
for seed in seeds: 
    print("seed:", seed)
    soil = find_source(seed_to_soils_sets, int(seed))
    fertilizer = find_source(soil_to_fertilizer_sets, soil)
    water = find_source(fertilizer_to_water_sets, fertilizer)
    light = find_source(water_to_light_sets, water)
    temperature = find_source(light_to_temperature_sets, light)
    humidity = find_source(temperature_to_humidity_sets, temperature)
    location = find_source(humidity_to_location_sets, humidity)

    if location < min_location:
        min_location = location
       
print(min_location)
"""
print(find_string_location_and_text_before_empty_line(input, "soil-to-fertilizer map:"))
print(find_string_location_and_text_before_empty_line(input, "fertilizer-to-water map:"))
print(find_string_location_and_text_before_empty_line(input, "water-to-light map:"))
print(find_string_location_and_text_before_empty_line(input, "light-to-temperature map:"))
print(find_string_location_and_text_before_empty_line(input, "temperature-to-humidity map:"))
print(find_string_location_and_text_before_empty_line(input, "humidity-to-location map:"))
"""

#1:06:26

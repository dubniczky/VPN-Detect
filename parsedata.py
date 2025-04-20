# Parses the data from the countries and timezones files

import re
import json

# Load timezones

timezones : dict[str, str] = dict()
with open('data/timezones.txt', 'r') as f:
    for line in f:
        match = re.match(r'([\w,]+)\s+([\w\+\d-]+)\s+([\w\/]+)', line)
        if match:
            country_code = match.group(1).split(',')[0] # Handle multiple country codes
            iana = match.group(3)
            timezones[iana] = country_code
        else:
            print(f"Failed to parse line: {line}")
            continue

# Load countries
with open('data/countries.json', 'r') as f:
    countries = json.load(f)

ccs = dict()
for country in countries:
    name = country['name']
    flag = country['flag']
    code = country['code']
    ccs[code] = {
        'name': name,
        'flag': flag
    }


# Final dictionary will contain two keys: 'countries' and 'timezones'
# Timezones will map from iana names to country codes
# Countries will map from country codes to country names/emojis

final_data = {
    'countries': ccs,
    'timezones': timezones
}
# Save the final data to a JSON file
with open('mapping.json', 'w') as f:
    json.dump(final_data, f)
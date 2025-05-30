import waveassist
import random

waveassist.init()

# Fetch the list of stored fortunes from WaveAssist's data storage
fortunes = waveassist.fetch_data('fortunes')

# Select a random fortune for today
today_fortune = random.choice(fortunes)

# Display the selected fortune
print("Your fortune for today:", today_fortune)

##You can also email this to yourself.

# Save for future work
waveassist.store_data('today_fortune', today_fortune)

# Import the WaveAssist SDK to interact with your project
import waveassist
# Initialize WaveAssist
waveassist.init()

# Define a list of fortune messages to be stored
fortunes = [
    "Today is your lucky day!",
    "Curiosity leads to breakthroughs.",
    "Take a deep breath and smile.",
    "Be bold. Fortune favors the brave!",
    "Patience is a virtue.",
    "Every day is a fresh start."
    "Your hard work will pay off soon.",
    "Embrace the challenges ahead.",
    "A new opportunity is on the horizon.",
    "Trust your instincts; they are usually right.",
    "A positive mindset brings positive outcomes.",
    "You will find joy in unexpected places.",
    "Beware of false friends.",
    "Not all that glitters is gold.",
    "Sometimes, the hardest battles are within.",
    "Change is the only constant.",
]

# Store the list of fortunes in WaveAssist's data storage under the key 'fortunes'
waveassist.store_data('fortunes', fortunes)

# Print confirmation with the stored fortunes
print("Stored Fortunes:", fortunes)

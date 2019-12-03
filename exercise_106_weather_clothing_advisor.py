# Make a weather/clothing game
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
user_input = input('What is the weather like today?')
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'

if user_input == 'sunny':
    print('Take your shorts!')
elif user_input == 'rainy':
    print('Take your umbrella')
elif user_input == 'stormy':
    print('Take a rain coat')
elif user_input == 'rainy and stormy':
    print('Stay home!')
else:
    print("Sorry, I didn't quite catch that")
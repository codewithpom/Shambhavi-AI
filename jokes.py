import pyjokes
import random
# using get_jokes() to generate a whole list of jokes
# language is german
# category is twister
list_of_jokes = pyjokes.get_jokes(language="en", category="all")

# traversing through the generated list of jokes
# Range of i may change, depending on the number of jokes
# you want to display

rank = random.randint(1, 100)


def jokes():
	return list_of_jokes[rank]

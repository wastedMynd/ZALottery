# Import Dependencies

import pandas as pd

from matplotlib import pyplot as plt

import random

def show_analysis():

    # Get Frequency of Drawn Numbers For The Year 2020

    numbers = [number for number in range(1, 51)]  # numbers from 1 to 50

    random_samples = 100

    frequencies = [random.randint(0, random_samples) for _ in range(50)]

    drawn_numbers_and_their_frequency = {numbers[index]: frequencies[index] for index in range(len(numbers))}

    print(f"{drawn_numbers_and_their_frequency = }")

    # Coronation of Min & Max between drawn_numbers_and_their_frequency

    associated_number_to_minimum_frequency = 1

    minimum_frequency = drawn_numbers_and_their_frequency[associated_number_to_minimum_frequency]

    print(f"staring {associated_number_to_minimum_frequency = } and {minimum_frequency = }")

    for number in range(2, len(numbers)):

        potential_minimum_frequency = drawn_numbers_and_their_frequency[number]

        if potential_minimum_frequency < minimum_frequency:
            minimum_frequency = potential_minimum_frequency
            associated_number_to_minimum_frequency = number

    print(f"ending {associated_number_to_minimum_frequency = } and {minimum_frequency = }")

    associated_number_to_maximum_frequency = 1

    maximum_frequency = drawn_numbers_and_their_frequency[associated_number_to_maximum_frequency]

    print(f"staring {associated_number_to_maximum_frequency = } and {maximum_frequency = }")

    for number in range(2, len(numbers)):

        potential_maximum_frequency = drawn_numbers_and_their_frequency[number]

        if potential_maximum_frequency > maximum_frequency:
            maximum_frequency = potential_maximum_frequency
            associated_number_to_maximum_frequency = number

    print(f"ending {associated_number_to_maximum_frequency = } and {maximum_frequency = }")

    # Map associated_number_to_min_max_frequencies

    min_max_numbers = [associated_number_to_minimum_frequency, associated_number_to_maximum_frequency]

    min_max_frequencies = [minimum_frequency, maximum_frequency]

    # Add Title and Labels to the Graph

    plt.title("Frequency of Drawn Numbers For The Year 2020")

    xlabel = "Drawn Numbers"

    plt.xlabel(xlabel)

    ylabel = "Frequency"

    plt.ylabel(ylabel)

    # Plot a drawn_numbers_and_their_frequency, Dotted Graph Represantaion,

    plt.plot(numbers, frequencies, "o")

    # Plot a Min and Max Frequency, Line Graph Represantaion.

    plt.plot(min_max_numbers, min_max_frequencies)

    # Plot 1st to last, Line Graph Represantaion.

    plt.plot([numbers[0],frequencies[0]], [numbers[len(numbers)-1],frequencies[len(frequencies)-1]])

    #plt.plot([numbers[len(numbers)-1],frequencies[len(frequencies)-1]],[numbers[0],frequencies[0]])

    # add legend to the graph

    legend = [
        f"This is {xlabel} vs {ylabel}",
         "This is Min and Max Number Frequencies",
         "This is 1st to last",
         #"This is last to 1st",
    ]

    plt.legend(legend)

    # show the graph

    plt.show()

if __name__ == '__main__':
    show_analysis()
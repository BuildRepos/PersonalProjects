import math
import time
import numpy as np
import random

# the base method is the hill climb search
# need a data structure to hold the states
# a list for the maintained, and separate lists for the mutated and crossovers
# side note, check out genetic programming

# use the textbook, slides, reserach, do what you gotta do to understand and implement in code.
# get the gist of how the algorithm works, get all the help you can get, and work it
# need several binary vecttors
populationstates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                    61, 62, 63]  # lists the 63 states


# print(populationstates.bin()) #need to convert the int values to binary
# actually have to do this yourself. use a high level API(&/or sample code from professsor)
# then make it into a list
# fitness function before genetic

def Decimal_to_binary(int):
    # binary_to_deimal in reverse
    binary_value = [0, 0, 0, 0, 0, 0]

    # for n in

    def binary_to_Decimal(binary_array):  # previously named binary_to_Decimal(binary_array)
        decimal_value = 0
        for bit in binary_array:
            decimal_value = (decimal_value << 1) | bit
        return decimal_value

    print(binary_to_Decimal([0, 0, 0, 0, 0, 1]))

    def decimal_to_binary(decimal_value):
        return [int(bit) for bit in bin(decimal_value)[2:].zfill(6)]


def crossover(c1, c2):
    # Generate a random index for crossover
    crossover_point = random.randint(1, len(c1) - 1)

    # Perform crossover
    offspring1 = c1[:crossover_point] + c2[crossover_point:]
    offspring2 = c2[:crossover_point] + c1[crossover_point:]

    return offspring1, offspring2

    # Example usage:


solution1 = [0, 0, 0, 1, 0, 1]
solution2 = [0, 0, 1, 1, 1, 1]
offspring1, offspring2 = crossover(solution1, solution2)
print("Offspring 1:", offspring1)
print("Offspring 2:", offspring2)



def fitness(c):
    decimal_value = 0
    for bit in c:
        decimal_value = (decimal_value << 1) | bit

    squared_decimal_value = decimal_value ** 2
    return squared_decimal_value


def random_selection(population, fitness):
    return random(populationstates)

# crossover(c1, c2):
# mutation - uses random numbers,
# will take in vector c, and p_m(possibility of mutation)\

def selection(population):
    # Randomly select individuals from the population based on their fitness values
    selected_population = [random_selection(population, fitness) for _ in range(len(population))]
    return selected_population

def mutation(c, p_m):
    mutated_c = []
    for bit in c:
        if random.random() < p_m:
            # Flip the bit if mutation occurs
            mutated_c.append(1 - bit)
        else:
            mutated_c.append(bit)
    return mutated_c

def check(population):
    for individual in population:
        if fitness(individual) == 0:
            return True
    return False

def evolution(population, p_m):
    n_generation = 0
    while not check(population):
        # Selection
        population = selection(population)

        # Crossover
        offspring_list = []
        for i in range(0, len(population), 2):
            c1, c2 = population[i], population[i + 1]
            offspring = crossover(c1, c2)
            offspring_list.extend(offspring)
        population += offspring_list

        # Mutation
        new_population = []
        for c in population:
            new_population.append(mutation(c, p_m))
        population = new_population

        n_generation += 1

    return n_generation

def genetic_algorithm(population, fitness_fn, mutation_rate=0.05, max_generations=1000):
    for generation in range(max_generations):
        new_population = []
        for _ in range(len(populationstates)):
            # Selection
            x = random_selection(population, fitness)
            y = random_selection(population, fitness)

            # Reproduction
            child = crossover(x, y)

            # Mutation
            if random.random() < mutation_rate:
                child = mutation(child)

            new_population.append(child)

        population = new_population
        target_fitness = 1;
        # Check for termination criteria
        if any(fitness_fn(individual) >= target_fitness for individual in population):
            break

    # Return the best individual in the final population
    return max(population, key=fitness_fn)


#def GENETIC_ALGORITHM(population, FITNESS_FN):
 #   return population


print(fitness([1, 0, 1, 0, 1, 1]))  # printing none. we have us an issue.
# issue is now resolved


print(crossover([0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0]))

print(genetic_algorithm(10, fitness_fn=[0,0,0,0,0,1], mutation_rate= 0.05))
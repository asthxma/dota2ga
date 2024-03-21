import matplotlib.pyplot as plt
import random
from geneticalgorithm.Data import preprocess_data
from geneticalgorithm.GeneticAlgorithm import genetic_algorithm

# Load and preprocess data
file_path = 'dataset\dota2_heroes.csv'
df, hero_df, total_fit= preprocess_data(file_path)
hero_data = hero_df.to_dict(orient='records')

# Initialize population
pop_size = 10
population = [random.sample(hero_data[:-1], 5) for _ in range(pop_size)]

# Set algorithm parameters
target_positions = ['safelane', 'midlane', 'offlane', 'soft support', 'hard support']
generations = 10
tournament_size = 3
crossover_rate = 0.8
mutation_rate = 0.1

# Run genetic algorithm
result, temp_result = genetic_algorithm(population, hero_data, target_positions, generations, tournament_size, crossover_rate, mutation_rate, pop_size)

# Print and visualize results
print("Individu Terbaik:")
for hero in result:
    print(f"Name: {hero['hero']}, Lane: {hero['primary_role']}, Role: {hero['fight_role']}")

# Plot fitness progress for both strategies on the same graph
plt.plot((temp_result / total_fit) * 100, label="Fitness")

plt.title("Fitness Progress")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()  # Add legend to differentiate the lines
plt.show()
import math
def get_number_ofbuildings():
  """Prompts the user to enter the number of buildings."""
  num_buildings = int(input("Enter the number of buildings: "))
  return num_buildings

def get_production_times(num_buildings):
  """Gets production times for each building from the user."""
  production_times = []
  for i in range(num_buildings):
    production_time = float(input(f"Enter production time for building {i+1}: "))
    production_times.append(production_time)
  return production_times

def calculate_building_ratio(production_times):
  """Calculates building ratio based on production times."""
  # Find the shortest production time (building 1)
  shortest_time = min(production_times)
  building_1_indices = []
  # Find all building indices with the shortest production time
  for i, time in enumerate(production_times):
    if time == shortest_time:
      building_1_indices.append(i)
  # Count the number of buildings with the shortest production time
  building_2_count = len(building_1_indices)
  return building_1_indices, building_2_count

def calculate_needed_shortest_buildings(production_times, shortest_time):
  """Calculates the number of shortest time buildings needed."""
  # Calculate the total production time for buildings excluding the shortest
  total_longer_production_time = sum(time for time in production_times if time > shortest_time)
  # Minimum number of shortest time buildings needed to keep the flow going
  min_buildings_needed = math.ceil(total_longer_production_time / shortest_time)
  return min_buildings_needed

if __name__ == "__main__":
  num_buildings = get_number_ofbuildings()
  production_times = get_production_times(num_buildings)
  building_1_indices, building_2_count = calculate_building_ratio(production_times)
  shortest_time = min(production_times)
  min_buildings_needed = calculate_needed_shortest_buildings(production_times, shortest_time)

  print("Number of buildings:", num_buildings)
  print("Production times:", production_times)
  print("Building(s) with shortest production time index(es):", building_1_indices)
  print("Number of buildings with the same shortest production time:", building_2_count)
  print(f"Minimum number of buildings with shortest production time needed:", min_buildings_needed)

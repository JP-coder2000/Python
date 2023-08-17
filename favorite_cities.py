class City:
    def __init__(self,name,country,population,landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

nyc = City("New York City", "United States", 340000000, "Statue of liberty")

print(vars(nyc))
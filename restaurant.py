class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        # Implement the logic to get unique customers who have reviewed this restaurant
        pass

    def average_star_rating(self):
        # Implement the logic to calculate the average star rating for this restaurant
        pass



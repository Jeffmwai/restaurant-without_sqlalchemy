# Yelp-style Domain - Object Relations Code Challenge

This project simulates a Yelp-style domain with three models: `Restaurant`, `Customer`, and `Review`. The models have various methods to handle relationships and aggregate information.

## Project Structure

- `customer.py`: Defines the `Customer` class with methods for handling customer information.
- `restaurant.py`: Defines the `Restaurant` class with methods for handling restaurant information.
- `review.py`: Defines the `Review` class with methods for handling reviews.

## Classes and Methods

### Customer

- `__init__(given_name, family_name)`: Initializes a new customer instance.
- `given_name()`: Returns the customer's given name.
- `family_name()`: Returns the customer's family name.
- `full_name()`: Returns the full name of the customer.
- `all()`: Returns all customer instances.
- `num_reviews()`: Returns the total number of reviews authored by a customer.
- `find_by_name(name)`: Finds a customer by their full name.
- `find_all_by_given_name(name)`: Finds all customers with a given name.

### Restaurant

- `__init__(name)`: Initializes a new restaurant instance.
- `name()`: Returns the restaurant's name.
- `all()`: Returns all restaurant instances.
- `reviews()`: Returns a list of all reviews for that restaurant.
- `customers()`: Returns a unique list of all customers who have reviewed a particular restaurant.
- `average_star_rating()`: Returns the average star rating for a restaurant based on its reviews.

### Review

- `__init__(customer, restaurant, rating)`: Initializes a new review instance.
- `rating()`: Returns the rating for a restaurant.
- `all()`: Returns all reviews.
- `customer()`: Returns the customer object for that review.
- `restaurant()`: Returns the restaurant object for that given review.

## Usage

1. Clone the repository.
2. Run your test cases or create new instances to interact with the classes.
3. Modify the classes as needed for your project.

## License

This project is licensed under the [MIT License](LICENSE).

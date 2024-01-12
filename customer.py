class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def num_reviews(self):
        # Implement the logic to count the number of reviews by this customer
        pass

    @classmethod
    def find_by_name(cls, name):
        # Implement the logic to find a customer by their full name
        pass

    @classmethod
    def find_all_by_given_name(cls, name):
        # Implement the logic to find all customers with a given name
        pass



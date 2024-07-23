class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        # I use this order in initializate default value for not using "else"
        self.comfort_class = comfort_class
        if not 1 <= comfort_class <= 7:
            self.comfort_class = 1

        self.clean_mark = clean_mark
        if not 1 <= clean_mark <= 10:
            self.clean_mark = 1

        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        if not 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = 1.0

        self.clean_power = clean_power
        if not 1 <= clean_power <= 10:
            self.clean_power = 1

        self.average_rating = average_rating
        if not 1.0 <= average_rating <= 5.0:
            self.average_rating = 1.0

        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        # sorted cars, who car_station can wash
        washes = [car for car in cars if car.clean_mark < self.clean_power]
        # calculate income
        income = [self.calculate_washing_price(car) for car in washes]
        # washing sorted car
        for car in washes:
            self.wash_single_car(car)
        return round(sum(income), 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1
        )

    def rate_service(self, rate: int) -> None:
        self.average_rating = (
            round((self.average_rating * self.count_of_ratings + rate)
                  / (self.count_of_ratings + 1), 1)
        )
        self.count_of_ratings += 1

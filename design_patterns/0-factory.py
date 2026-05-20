#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def mode(self):
        pass


class Bus(Vehicle):
    def mode(self):
        return "road"


class Train(Vehicle):
    def mode(self):
        return "rails"


class Bike(Vehicle):
    def mode(self):
        return "lane"


class Scooter(Vehicle):
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    def __init__(self):
        self._registry = {}

    def register_kind(self, name, cls):
        self._registry[name] = cls

    def create(self, kind):
        cls = self._registry.get(kind)

        if cls is None:
            raise ValueError(f"Unknown vehicle type: {kind}")

        return cls()


def main():
    factory = VehicleFactory()

    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()

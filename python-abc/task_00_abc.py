#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Create class"""


class Animal(ABC):
    """Implement the sound method"""
    @abstractmethod
    def sound(self):
        pass


"""Create Subclass Dog"""


class Dog(Animal):
    """Implement the sound method in the Dog class"""
    def sound(self):
        return ("Bark")


"""Create Subclass Cat"""


class Cat(Animal):
    """Implement the sound method in the Cat class"""
    def sound(self):
        return ("Meow")

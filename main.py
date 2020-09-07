from product import Product, ProductCategory as Category
from random import randint
from typewriter import *
from colorama import Fore

def phone(itemCode, description, price) -> Product:
  return Product(Category.PHONE, itemCode, description, price)

def tablet(itemCode, description, price) -> Product:
  return Product(Category.TABLET, itemCode, description, price)

def simCard(itemCode, description, price) -> Product:
  return Product(Category.SIM_CARD, itemCode, description, price)

def case(itemCode, description, price) -> Product:
  return Product(Category.CASE, itemCode, description, price)

def charger(itemCode, description, price) -> Product:
  return Product(Category.CHARGER, itemCode, description, price)

products = [
  phone("BPCM", "Compact", "29.99"),
  phone("BPSH", "Clam Shell", "49.99"),
  phone("RPSS", "RoboPhone – 5-inch screen and 64 GB memory", "199.99"),
  phone("RPLL", "RoboPhone – 6-inch screen and 256 GB memory", "499.99"),
  phone("YPLS", "Y-Phone Standard – 6-inch screen and 64 GB memory", "549.99"),
  phone("YPLL", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "649.99"),
  tablet("YPLL", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "649.99"),
]

randomProduct = randint(1, len(products))

typewriter(f"{products[randomProduct].description}", Fore.BLUE)
typewriter(f" - £{products[randomProduct].price}")





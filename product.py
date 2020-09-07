from enum import Enum

class ProductCategory(Enum):
  PHONE = 'Phone'
  TABLET = 'Tablet'
  SIM_CARD = 'SIM Card'
  CASE = 'Case'
  CHARGER = 'Charger'

class Product:
  def __init__(self, category: ProductCategory, itemCode, description, price):
    self.category = category
    self.itemCode = itemCode
    self.description = description
    self.price = price

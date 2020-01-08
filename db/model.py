from . import db

class User(db.Model):
    __tablename__ = 'user_table'
    id = ...
    name = ...
    email = ...

    def set_password(self, password):
        ...

    def check_password(self, password):
        ...




class Shop(db.Model):
    __tablename__ = 'shop_table'
    id = ...
    name = ...

class Item:
    __tablename__ = 'item_name'
    id = ...
    name = ...

# item availability in a shop
# vailability inside the shop
# Basket
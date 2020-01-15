from . import db

class UserModel(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def set_password(self, password):
        ...

    def check_password(self, password):
        ...


# class Shop(db.Model):
#     __tablename__ = 'shop_table'
#     id = ...
#     name = ...
#
# class Item:
#     __tablename__ = 'item_name'
#     id = ...
#     name = ...

# item availability in a shop
# vailability inside the shop
# Basket
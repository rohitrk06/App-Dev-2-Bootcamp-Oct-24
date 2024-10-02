from applications.database import db
from flask_security import UserMixin, RoleMixin

class User(db.Model, UserMixin):
    username = db.Column(db.String(100),primary_key=True)
    email = db.Column(db.String(255),unique=True,nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    is_approved = db.Column(db.Boolean(),nullable=False,default=False)

    roles = db.relationship('Role', secondary='user_roles', 
                            backref=db.backref('users', lazy=True))

    # Required Fields for Flask-Security to work properly
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    fs_token_uniquifier = db.Column(db.String(255),unique=True)
    active = db.Column(db.Boolean())

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.username'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),nullable=False)


class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(255), nullable=False)
    category_description = db.Column(db.String(255), nullable=False)

    products = db.relationship('Products', backref='categories')


class Products(db.Model):
    product_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),nullable=False)
    description = db.Column(db.String(100),nullable=True)
    selling_price = db.Column(db.Float,nullable=False)
    stock = db.Column(db.Integer,nullable=False)
    manufacture_date = db.Column(db.Date,nullable=False)
    expiry_date = db.Column(db.Date,nullable=True)
    cost_price = db.Column(db.Float,nullable=False)
    image_url = db.Column(db.String(100),nullable=True)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.category_id'))

class Cart(db.Model):
    card_id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),db.ForeignKey('user.username'))
    product_id = db.Column(db.Integer,db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer,nullable=False)

class Requests(db.Model):
    request_id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),db.ForeignKey('user.username'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.category_id'),nullable=True)
    request_type = db.Column(db.String(20),nullable=False)
    request_date = db.Column(db.Date,nullable=False)
    status = db.Column(db.String(20),nullable=False)
    new_category_name = db.Column(db.String(40),nullable=True)
    new_category_description = db.Column(db.String(100),nullable=True)

    #Relationships
    catergory = db.relationship('Categories',backref='requests',lazy=True)

    def __repr__(self):
        return f'<Request {self.catergory_id} - {self.request_type}>'
    

class PurchaseHistory(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,nullable=False)
    username = db.Column(db.String(30),db.ForeignKey('user.username'))
    product_id = db.Column(db.Integer,db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer,nullable=False)
    purchase_date = db.Column(db.Date,nullable=False)
    total_price = db.Column(db.Float,nullable=False)

    #Relationships
    product = db.relationship('Products',backref='purchase_history',lazy=True)
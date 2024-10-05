from flask_restful import Resource, reqparse
from flask import jsonify, request, make_response
from applications.database import db
from applications.models import *
from flask_security import auth_token_required, roles_accepted, roles_required, current_user
from datetime import datetime

class AllStoreManager(Resource):
    @auth_token_required
    @roles_required('admin')
    def get(self):
        users = User.query.all()
        final_respone = []
        for i in users:
            if 'store_manager' in [role.name for role in i.roles]:
                response = {
                    'username': i.username,
                    'email': i.email,
                    'address': i.address,
                    'is_approved': i.is_approved
                }
                final_respone.append(response)
        return make_response(jsonify(final_respone), 200)
    
class ApproveStoreManager(Resource):
    @auth_token_required
    @roles_required('admin')
    def put(self, username):
        try:
            user  = User.query.filter_by(username=username).first()
            if not user:
                return make_response(jsonify({'message': 'User not found'}), 404)
            
            user.is_approved = True
            db.session.commit()
            return make_response(jsonify({'message': 'User approved successfully'}), 200)
        except Exception as e:
            return make_response(jsonify({'message': 'Internal Server Error'}), 500)
        
class ViewAllCategories(Resource):
    @auth_token_required
    def get(self):
        categories = Categories.query.all()
        final_response = []
        for i in categories:
            response = {
                'category_id': i.category_id,
                'category_name': i.category_name,
                'category_description': i.category_description,
                'products':[
                    {
                        'product_id': j.product_id,
                        'name': j.name,
                        'description': j.description,
                        'selling_price': j.selling_price,
                        'stock': j.stock,
                        'manufacture_date': j.manufacture_date,
                        'expiry_date': j.expiry_date,
                        'cost_price': j.cost_price,
                        'image_url': j.image_url
                    } for j in i.products
                ]
            }
            final_response.append(response)
        return make_response(jsonify(final_response), 200)
    
class Category(Resource):
    @auth_token_required
    def get(self,category_id):
        # category = Categories.query.filter_by(category_id=category_id).first()
        category = Categories.query.get(category_id).first()
        if not category:
            return make_response(jsonify({'message': 'Category not found'}), 404)
        
        response = {
                'category_id': category.category_id,
                'category_name': category.category_name,
                'category_description': category.category_description
            }
        
        return make_response(jsonify(response), 200)
    
    @auth_token_required
    @roles_accepted('admin','store_manager')
    def post(self):
        request_data = request.get_json()

        category_name = request_data.get('category_name', None)
        category_description = request_data.get('category_description', None)

        if not category_name:
            return make_response(jsonify({'message': 'category_name is required'}), 400)
        
        category = Categories.query.filter_by(category_name=category_name).first()
        if category:
            return make_response(jsonify({'message': 'Category already exists'}), 400)

        if current_user.has_role('store_manager'):
            if not current_user.is_approved:
                return make_response(jsonify({'message': 'Store Manager is not approved yet'}), 401)
            
            try:
                new_category_request = Requests(username = current_user.username,
                                                request_type = 'new_category',
                                                request_date = datetime.now(),
                                                status = 'pending',
                                                new_category_name = category_name,
                                                new_category_description = category_description)
                db.session.add(new_category_request)
                db.session.commit()
                return make_response(jsonify({'message': 'Request sent successfully'}), 201)
            except Exception as e:
                return make_response(jsonify({'message': 'Internal Server Error'}), 500)
        else:
            try:
                category = Categories(category_name = category_name, 
                                      category_description = category_description)
                db.session.add(category)
                db.session.commit()
                return make_response(jsonify({'message': 'Category added successfully'}), 201)
            except Exception as e:
                return make_response(jsonify({'message': 'Internal Server Error'}), 500)

        
from flask_restful import Resource, reqparse
from flask import jsonify, request, make_response
from flask_security import hash_password, utils, auth_token_required
from applications.user_datastore import user_datastore
from applications.database import db


class UserRegistration(Resource):
    def post(self): 
        # request_data = request.get_json()
        # username = request_data['username']
        # return {'message': 'you are post request at User Registration', 'username': username}

        request_data = request.get_json()

        email = request_data.get('email', None)
        password = request_data.get('password', None)
        address = request_data.get('address', None)
        username = request_data.get('username', None)
        role = request_data.get('role', None)


        #Data Validation -- custom validation
        if not username or not username.isalnum():
            return make_response(jsonify({'message': 'username is required or Invalid username entered'}), 401)
        
        if not email or '@' not in email:
            return make_response(jsonify({'message': 'email is required or Invalid email Entered '}), 401)
        
        if not password or len(password) < 6:
            return make_response(jsonify({'message': 'password is required and should be atleast 6 characters'}), 401)
        
        if role not in ['admin', 'customer', 'store_manager']:
            return make_response(jsonify({'message': 'role is required and should be either customer or store_manager'}), 401)

        user = user_datastore.find_user(username=username)
        if user: 
            return make_response(jsonify({'message': 'User already exists with this username'}), 401)
        
        user = user_datastore.find_user(email=email)
        if user: 
            return make_response(jsonify({'message': 'User already exists with this email'}), 401)

        try:
            role = user_datastore.find_role(role)
            user = user_datastore.create_user(username = username,
                                              email = email,
                                              password = hash_password(password),
                                              address = address,
                                              roles = [role])
            
            user_datastore.commit()

            response = {
                'message': 'User successfully registered',
                'user' :{
                    'username': user.username,
                    'email': user.email,
                    'address': user.address,
                    'roles': [role.name for role in user.roles]
                }
            }

            return make_response(jsonify(response), 201)
        except Exception as e:
            response = {
                'message': 'Internal Server Error',
                'error': str(e)
            }
            return make_response(jsonify(response), 500)


class UserLogin(Resource):
    def post(self):
        request_data = request.get_json()
        username = request_data.get('username', None)
        password = request_data.get('password', None)

        if not username or not password:
            return make_response(jsonify({'message': 'username and password are required'}), 401)
        
        user = user_datastore.find_user(username=username)
        if not user:
            return make_response(jsonify({'message': 'User not found'}), 401)
        
        if not utils.verify_password(password, user.password):
            return make_response(jsonify({'message': 'Invalid Password'}), 401)
        
        # if user.is_approved == False and user.roles[0].name == 'store_manager':
        #     return make_response(jsonify({'message': 'Store Manager is not approved yet'}), 401)

        try:
            utils.login_user(user)
            auth_token = user.get_auth_token()

            response={
                'message': 'User successfully logged in',
                "login_credentials": {
                    'username': user.username,
                    'roles': [role.name for role in user.roles],
                    'auth_token': auth_token
                },
            }

            return make_response(jsonify(response), 200)
        
        except Exception as e:
            response = {
                'message': 'Internal Server Error',
                'error': str(e)
            }
            return make_response(jsonify(response), 500)
        
class UserLogout(Resource):
    @auth_token_required
    def post(self):
        utils.logout_user()
        response = {
            'message': 'User successfully logged out'
        }
        return make_response(jsonify(response), 200)
        

            
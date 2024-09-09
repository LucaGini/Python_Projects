from flask import Flask, jsonify, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime, timedelta
import enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['JWT_SECRET_KEY'] = '12345678'

db = SQLAlchemy(app)
jwt = JWTManager(app)

class ExpenseCategory(enum.Enum):
    GROCERIES = 'groceries'
    LEISURE = 'leisure'
    ELECTRONICS = 'electronics'
    UTILITIES = 'utilities'
    CLOTHING = 'clothing'
    HEALTH = 'health'
    OTHERS = 'others'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy='dynamic')

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.Enum(ExpenseCategory), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    user_id = get_jwt_identity()
    filter_by = request.args.get('filter_by', 'all')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if filter_by == 'week':
        expenses = Expense.query.filter_by(user_id=user_id).filter(Expense.date >= datetime.utcnow() - timedelta(days=7)).all()
    elif filter_by == 'month':
        expenses = Expense.query.filter_by(user_id=user_id).filter(Expense.date >= datetime.utcnow() - timedelta(days=30)).all()
    elif filter_by == 'three_months':
        expenses = Expense.query.filter_by(user_id=user_id).filter(Expense.date >= datetime.utcnow() - timedelta(days=90)).all()
    elif filter_by == 'custom' and start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        expenses = Expense.query.filter_by(user_id=user_id).filter(Expense.date >= start_date, Expense.date <= end_date).all()
    else:
        expenses = Expense.query.filter_by(user_id=user_id).all()

    return jsonify([expense.to_dict() for expense in expenses])

@app.route('/expenses', methods=['POST'])
@jwt_required()
def create_expense():
    user_id = get_jwt_identity()
    description = request.json.get('description', None)
    amount = request.json.get('amount', None)
    category = request.json.get('category', None)

    if not description or not amount or not category:
        return jsonify({'message': 'Description, amount, and category are required'}), 400

    try:
        category = ExpenseCategory(category)
    except ValueError:
        return jsonify({'message': 'Invalid expense category'}), 400

    expense = Expense(description=description, amount=amount, category=category, user_id=user_id)
    db.session.add(expense)
    db.session.commit()

    return jsonify(expense.to_dict()), 201

@app.route('/expenses/<int:expense_id>', methods=['PUT'])
@jwt_required()
def update_expense(expense_id):
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()

    if not expense:
        return jsonify({'message': 'Expense not found'}), 404

    description = request.json.get('description', expense.description)
    amount = request.json.get('amount', expense.amount)
    category = request.json.get('category', expense.category.value)

    try:
        category = ExpenseCategory(category)
    except ValueError:
        return jsonify({'message': 'Invalid expense category'}), 400

    expense.description = description
    expense.amount = amount
    expense.category = category
    db.session.commit()

    return jsonify(expense.to_dict()), 200

@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
@jwt_required()
def delete_expense(expense_id):
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()

    if not expense:
        return jsonify({'message': 'Expense not found'}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({'message': 'Expense deleted'}), 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
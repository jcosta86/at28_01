import sys
sys.path.append('.')
from flask import Flask, render_template, request, redirect

from src.controllers.category_controller import CategoryController
from src.models.category import Category


app = Flask(__name__)

name = 'olist'


CONTROLLER = CategoryController()


@app.route('/categories')
def categories():
    list_categories = CONTROLLER.read_all()
    return render_template('categories.html', name=name, categories=list_categories)


@app.route('/create_category')
def create_category_form():
    id_aux = request.args.get('id')
    if id_aux:
        category = CONTROLLER.read_by_id(int(id_aux))
        return render_template('create_category.html', update=True, category=category)
    return render_template('create_category.html')


@app.route('/category/create', methods=['POST'])
def create_category():
    name = request.form.get('name')
    description = request.form.get('description')
    new_category = Category(name, description)
    CONTROLLER.create(new_category)
    return redirect('/categories')


@app.route('/edit_category', methods=['POST'])
def edit_category():
    id_aux = int(request.form.get('id'))
    name = request.form.get('name')
    description = request.form.get('description')
    category = CONTROLLER.read_by_id(id_aux)
    category.name = name                                     
    category.description = description
    CONTROLLER.update(category)                                     
    return redirect('/categories')


@app.route('/delete_category')
def delete_category():
    id_aux = int(request.args.get('id'))
    category = CONTROLLER.read_by_id(id_aux)
    CONTROLLER.delete(category)
    return redirect('/categories')


@app.route('/')
def index():
    list_menu = [
    {'name': 'Categories',
     'route': '/categories'}
    ]   
    return render_template('index.html', name=name, list_menu=list_menu)


app.run(debug=True)

from flask import render_template, url_for, flash
from app import app, db
from models import items
from forms import queryform, itemform

@app.route('/')
def index():
	q = items.query.all()
	return render_template('index.html', items=q)

@app.route('/query/', methods=['GET', 'POST'])
def query_item():
	error = None
	form = queryform()
	if form.validate_on_submit():
		q = items.query.filter_by(name=form.name.data).all()
		if q:
			return render_template('query.html', form=form, items=q)
		else:
			error = "No items"
	return render_template('query.html', form=form, error=error)

@app.route('/add/', methods=['GET', 'POST'])
def add_item():
	error = None
	form = itemform()
	if form.validate_on_submit():
		try:
			i = items(name=form.name.data, description=form.description.data)
			db.session.add(i)
			db.session.commit()
			flash('Item added')
		except Exception as e:
			error = e
	return render_template('add.html', form=form, error=error)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
	error = None
	q = items.query.filter_by(id=id).first_or_404()
	form = itemform(obj=q)
	if form.validate_on_submit():
		try:
			q.name = form.name.data
			q.description = form.description.data
			db.session.commit()
			flash("Item updated")
		except Exception as e:
			error = e
	return render_template('edit.html', form=form, error=error)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_item(id):
	error = None
	q = items.query.filter_by(id=id).first_or_404()
	if q:
		try:
			db.session.delete(q)
			db.session.commit()
			flash("Item deleted")
		except Exception as e:
			error = e
	return render_template('query.html', error=error)
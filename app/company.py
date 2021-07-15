from flask import (Blueprint, flash, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db

bp = Blueprint('company', __name__)


@bp.route('/')
@login_required
def index():
	db = get_db()
	companies = db.execute(
		'SELECT * FROM companies ORDER BY name'
	).fetchall()
	return render_template('company/index.html', companies=companies)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
	if request.method == 'POST':
		name = request.form['name']
		error = None

		if not name:
			error = 'Name is required'

		if error is not None:
			flash(error)
		else:
			db = get_db()
			db.execute(
				'INSERT INTO companies (name) VALUES (?)', (name,)
			)
			db.commit()
			return redirect(url_for('company.index'))
	return render_template('company/create.html')


def get_company(id):
	company = get_db().execute(
		'SELECT * FROM companies WHERE id = ?', (id,)
	).fetchone()

	if company is None:
		abort(404, f"Company id {id} doesn't exist")

	return company


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
	company = get_company(id)

	if request.method == 'POST':
		name = request.form['name']
		error = None

		if not name:
			error = 'Name is required'

		if error is not None:
			flash(error)
		else:
			db = get_db()
			db.execute(
				'UPDATE companies SET name = ? WHERE id = ?', (name, id)
			)
			db.commit()
			return redirect(url_for('company.index'))
	return render_template('company/update.html', company=company)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
	get_company(id)
	db = get_db()
	db.execute(
		'DELETE FROM companies WHERE id = ?', (id,)
	)
	db.commit()
	return redirect(url_for('company.index'))

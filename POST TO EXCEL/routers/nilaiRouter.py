from flask import Blueprint, render_template
from controllers.nilaiController import NilaiController

nilai_blueprint = Blueprint('nilai', __name__)

@nilai_blueprint.route('/')
def welcome():
    return render_template('welcomeView.html')

@nilai_blueprint.route('/nilai')
def index():
    return render_template('nilaiView.html')

@nilai_blueprint.route('/save_data', methods=['POST'])
def save_data():
    return NilaiController.save_data()

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, DateField, SelectField, FileField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length

from models import Cars, Worker, Garage, Details, Accounts


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=45)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=45)])
    isworker = BooleanField('Are you a Base402 employee?', default=False)
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=4, max=45)])
    second_name = StringField('Second Name', validators=[DataRequired(), Length(min=4, max=45)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=4, max=45)])
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class CreateLotForm(FlaskForm):
    make = StringField(validators=[DataRequired(), Length(min=2, max=45)])
    model = StringField(validators=[DataRequired(), Length(min=2, max=45)])
    category = SelectField(validators=[DataRequired()], coerce=str, choices=['Super', 'Sport', 'Coupe', 'Sedan', 'SUV'])
    vin = StringField(validators=[DataRequired(), Length(min=17, max=17)])
    plates = StringField(validators=[DataRequired(), Length(min=6, max=6)])
    production_date = DateField(format='%Y-%m-%d', validators=[DataRequired()])
    image = FileField('Upload File', validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg'], 'Images only!')])


class CreateRepairWorkForm(FlaskForm):

    car = SelectField('Car', coerce=int, validators=[DataRequired()])
    worker = SelectField('Worker', coerce=int, validators=[DataRequired()])
    garage = SelectField('Garage', coerce=int, validators=[DataRequired()])
    detail = SelectField('Detail', coerce=int, validators=[DataRequired()])
    start_date = DateField(format='%Y-%m-%d', validators=[DataRequired()])
    type = SelectField(validators=[DataRequired()], coerce=str, choices=['Замена', 'Ремонт', 'Очистка', 'Покраска'])

    def __init__(self, *args, **kwargs):
        super(CreateRepairWorkForm, self).__init__(*args, **kwargs)
        self.car.choices = [(car.idCars, f"{car.Make}, {car.Plates}") for car in Caars.query.all()]
        self.worker.choices = [(worker.idWorker, f"{worker.Surname}, {worker.First_Name}") for worker in Worker.query.all()]
        self.garage.choices = [(garage.idGarage, garage.Number) for garage in Garage.query.all()]
        self.detail.choices = [(detail.idDetails, detail.Type) for detail in Details.query.all()]


class CreateMileageForm(FlaskForm):
    car_id = SelectField('Car', coerce=int, validators=[DataRequired()])
    mileage = DecimalField('Mileage', validators=[DataRequired()])
    date = DateField(format='%Y-%m-%d', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(CreateMileageForm, self).__init__(*args, **kwargs)
        self.car_id.choices = [(car.idCars, f"{car.Make}, {car.Plates}") for car in Cars.query.all()]
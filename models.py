from flask_login import UserMixin
from sqlalchemy_media import Attachment
from config import db


class Accounts(UserMixin, db.Model):
    __tablename__ = 'accounts'
    idAccounts = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(45), unique=True, nullable=True)
    password = db.Column(db.String(45), nullable=True)



class Cars(db.Model, Attachment):
    __tablename__ = 'cars'
    idCars = db.Column(db.Integer, primary_key=True)
    Make = db.Column(db.String(45), unique=True, nullable=True)
    Model = db.Column(db.String(45), nullable=True)
    Plates = db.Column(db.String(6), nullable=True)
    Production_Date = db.Column(db.Date, nullable=True)
    Vehicle_Category = db.Column(db.String(45), nullable=True)
    VIN = db.Column(db.String(17), nullable=True)
    Image_name = db.Column(db.String(45), nullable=True)
    Image_path = db.Column(db.String(255), nullable=True)
    Repair_Works = db.relationship('Repair_Works', backref='car', lazy=True)


class Worker(db.Model):
    __tablename__ = 'worker'
    idWorker = db.Column(db.Integer, primary_key=True)
    Account_ID = db.Column(db.Integer, db.ForeignKey('accounts.idAccounts'))
    First_Name = db.Column(db.String(45), nullable=True)
    Second_Name = db.Column(db.String(45), nullable=True)
    Surname = db.Column(db.String(45), nullable=True)


class Mileage(db.Model):
    __tablename__ = 'mileage'
    idMileage = db.Column(db.Integer, primary_key=True)
    Car_ID = db.Column(db.Integer, db.ForeignKey('cars.idCars'))
    Mileage = db.Column(db.Integer, nullable=True)
    Date = db.Column(db.Date, nullable=True)


class Details(db.Model):
    __tablename__ = 'details'
    idDetails = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(45), nullable=True)
    Count = db.Column(db.Integer, nullable=True)


class Garage(db.Model):
    __tablename__ = 'garage'
    idGarage = db.Column(db.Integer, primary_key=True)
    Number = db.Column(db.Integer, nullable=True)


class Repair_Works(db.Model):
    __tablename__ = 'repair_works'
    idRepairWorks = db.Column(db.Integer, primary_key=True)
    Car = db.Column(db.Integer, db.ForeignKey('cars.idCars'))
    Worker = db.Column(db.Integer, db.ForeignKey('worker.idCars'))
    Garage = db.Column(db.Integer, db.ForeignKey('garage.idGarage'))
    Detail = db.Column(db.Integer, db.ForeignKey('details.idDetails'))
    Start_Date = db.Column(db.Date, nullable=True)
    Type = db.Column(db.String(45), nullable=True)
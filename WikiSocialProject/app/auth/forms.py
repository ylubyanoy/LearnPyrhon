from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Usersdb


class LoginForm(FlaskForm):
    username = StringField("Пользователь", validators=[DataRequired(), Length(1, 100)])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(1, 10)])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Length(1, 65), Email()])
    username = StringField("Пользователь", validators=[
        DataRequired(), Length(1, 100), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Имя пользователя должно состоять из букв, цифр, точек и подчеркиваний')])
    password = PasswordField("Пароль", validators=[
        DataRequired(), EqualTo('password2', message='Пароли должны совпадать'), Length(1, 10)])
    password2 = PasswordField("Подтверждение", validators=[DataRequired(), Length(1, 10)])
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, field):
        if Usersdb.query.filter_by(email=field.data).first():
            raise ValidationError('Адрес электронной почты используется')

    def validate_username(self, field):
        if Usersdb.query.filter_by(user_name=field.data).first():
            raise ValidationError('Имя пользователя используется')




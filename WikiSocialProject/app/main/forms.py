from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, SubmitField
from wtforms_components import read_only
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired(), Length(1, 200)])
    body = PageDownField("Статья", validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class EditProfileForm(FlaskForm):
    email = StringField("E-mail")
    username = StringField("Пользователь")
    company_name = StringField('Организация', validators=[Length(1, 65)])
    submit = SubmitField('Сохранить')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        read_only(self.username)
        read_only(self.email)

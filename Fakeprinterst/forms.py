from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Fakeprinterst.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao = SubmitField("Fazer login")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuario", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(8, 20)])
    confirmacao_senha = PasswordField("Confirmação de senha", validators=[DataRequired(), EqualTo("senha")])
    botao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail ja cadastrato, faça login para continuar")

class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")
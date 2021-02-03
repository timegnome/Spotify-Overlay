from wtforms import Form, StringField, validators, SelectField


class SubmissionForm(Form):
    background = SelectField('Background', choices =[('White','White'),('Black','Black')], default ='Black')

    size = SelectField('Size', choices =[('600',600), ('520',520), ('480',480), ('420',420), ('360',360), ('320',320)], default =480)

    color = StringField('Color Hex Value', [validators.required(), validators.length(max=7)])
    

from wtforms import Form, StringField, validators
from wtforms.validators import ValidationError
from wtforms.widgets import TextArea

class StoryForm(Form):
    content = StringField('Content', [validators.InputRequired()], widget=TextArea())

    def validate_content(self, content):
        text = content.data

        if len(text) <= 2:
            raise ValidationError('Post must contain at least 3 characters!')
        elif len(text) >= 280:
            raise ValidationError('Ooops that is more than 280 characters!')


class ReplyForm(Form):
    content = StringField('Content', [validators.InputRequired()], widget=TextArea())

    def validate_content(self, content):
        text = content.data

        if len(text) <= 2:
            raise ValidationError('Post must contain at least 3 characters!')
        elif len(text) >= 280:
            raise ValidationError('Ooops that is more than 280 characters!')
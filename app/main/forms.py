from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class Blog_Form(FlaskForm):

    title = StringField('What is the title?')
    category = SelectField('Choose the Post category', choices=[('Movie', 'movie-blog'), ('Sports', 'sports-blog'), ('Mathematics', 'maths-blog') ,('Health', 'health-blog'), ('Car', 'car-blogs'),('Music', 'music-blog'), ('random', 'random')])
    message = TextAreaField('Post')
    submit = SubmitField('Share Post')


class Comment_Form(FlaskForm):

    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')


# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')


from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100, widget=forms.TextInput)
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # for field in self.fields.values():
        #     field.widget.attrs.update({'class': 'input'})


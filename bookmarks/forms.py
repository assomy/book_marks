from django import  forms
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Password (Again)',
        widget=forms.PasswordInput()
    )
    def clean_password2(self):
        if 'password1' in self.clean_data:
        password1 = self.clean_data['password1']
        password2 = self.clean_data['password2']
        if password1 == password2:
        return password2
    raise forms.ValidationError('Passwords do not match.')



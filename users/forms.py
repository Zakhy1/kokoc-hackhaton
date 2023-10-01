from django import forms

from organisations.models import Organisation
from users.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ["email"]
        labels = {
            "email": ""
        }
        widgets = {
            'email': forms.EmailInput(attrs={"placeholder": "Введите email"})
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Password don't match")
        return cd["password2"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already in use.")
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "surname",
                  "department", "company", "profile_image", "post_index",
                  "address", "date_of_birth"]

    def clean(self):
        cleaned_data = super().clean()
        organisation = cleaned_data.get('company')
        department = cleaned_data.get('department')

        if organisation and department:
            if department.organisation != organisation:
                raise forms.ValidationError("Выбранный отдел не принадлежит выбранной организации.")

        return cleaned_data

from django import forms

from organisations.models import Fund, Organisation


class FundRegisterForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ["title", "description"]


class OrganisationRegisterForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ["title", "description", "OGRN"]

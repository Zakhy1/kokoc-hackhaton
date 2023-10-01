from django import forms

from events.models import EventProof


class EventConfirmForm(forms.ModelForm):
    class Meta:
        model = EventProof
        fields = ["screenshot"]

        labels = {
            "screenshot": "Скриншот с трекера"
        }

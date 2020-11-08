from django import forms

CHOICES = [('Bad','Bad'),('Average','Average'),('Good','Good'),('Excellent','Excellent')]

class SimpleForm(forms.Form):
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    experience = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=CHOICES,
    )


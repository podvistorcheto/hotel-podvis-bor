from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('TWIN', 'TWIN ROOM'),
        ('DBL', 'DOUBLE ROOM'),
        ('FAM', 'FAMILY ROOM'),
        ('DSUI', 'DELUXE SUITE'),
        ('APT', 'APARTMENT'),
        ('DAPT', 'DELUXE APARTMENT'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
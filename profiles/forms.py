from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'profile_full_name': 'Full Name',
            'profile_phone_number': 'Phone Number',
            'profile_postcode': 'Postal Code',
            'profile_town_or_city': 'Town or City',
            'profile_address_line1': 'Street Address 1',
            'profile_address_line2': 'Street Address 2',
            'profile_county': 'County',
            'profile_country': 'Country',
        }

        self.fields['profile_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
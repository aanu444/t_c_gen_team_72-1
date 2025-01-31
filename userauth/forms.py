import re
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ResetPassword(forms.Form): 

    new_password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'id':'new_password', 'type':'password', 'placeholder':'Enter new password'}))  # TODO: add length of password
    confirm_new_password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'id':'confirm_new_password', 'type':'password', 'placeholder':'Confirm new password'}))  # TODO: add length of password

    def clean(self):
        new_password = self.cleaned_data['new_password']

        if not bool(re.search(r'\d', new_password)):
            raise ValidationError(
                _('Password must contain at least one digit'))

        confirm_new_password = self.cleaned_data['confirm_new_password']

        if confirm_new_password != new_password:
            raise ValidationError(_('Passwords do not match'))

        return self.cleaned_data

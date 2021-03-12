from django import forms
from .models import HseOwner, Occupants, Staff


class HseOwnerForm(forms.ModelForm):

    class Meta:
        model = HseOwner
        fields = '__all__'
        labels = {
            'firstname': 'First Name',
            'id_number': 'ID. Number',
            'mobile_number': 'Mobile Number',
            'hse_number': 'Hse. Number'
        }

    def __init__(self, *args, **kwargs):
        super(HseOwnerForm, self).__init__(*args, *kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['hse_number'].empty_label = "Select"


class ResidentForm(forms.ModelForm):

    class Meta:
        model = Occupants
        fields = '__all__'
        labels = {
            'firstname': 'First Name',
            'hse_number': 'Hse. Number'
        }

    def __init__(self, *args, **kwargs):
        super(ResidentForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['hse_number'].empty_label = "Select"


class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = '__all__'
        labels = {
            'firstname': 'First Name',
            'id_number': 'ID. Number',
            'mobile_number': 'Mobile Number',

        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['position'].empty_label = "Select"

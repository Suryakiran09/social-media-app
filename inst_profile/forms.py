from django import forms
from .models import Profile

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = Profile
        fields = ['username', 'date_of_birth', 'photo']
        widgets = {
            'date_of_birth': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            
    def clean(self):
        cleaned_data = super().clean()
        photo = cleaned_data.get('photo')

        if photo and self.instance.photo and photo != self.instance.photo:
            # Delete the old image if a new one was provided
            self.instance.photo.delete()

        return cleaned_data
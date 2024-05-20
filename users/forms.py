from typing import Any
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password")

    def save(self,commit = True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

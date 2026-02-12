from django import forms 
from .models import *

class EventForm(forms.ModelForm):
    class Meta: 
        model=EventModel
        fields= '__all__'
        exclude=['created_by']
        widgets={
            'event_date':forms.DateInput(attrs={'type':'date'})
        }
        
# exclude use for separate model field
# widgets use for customise
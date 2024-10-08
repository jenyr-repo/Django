from django import forms
# from .models import Logger_New
shifts=(
    ("1","morning"),("2","afternoon"),("3","evening")
)
class InputForm(forms.Form):
    first_name= forms.CharField(max_length=200,required=False)
    last_name= forms.CharField(max_length=200,required=False)
    shift=forms.ChoiceField(choices=shifts)
    time_log=forms.TimeField(help_text="Enter the exact time")

# class LogForm(forms.ModelForm):
#     class Meta:
#         model=Logger_New
#         fields='__all__'


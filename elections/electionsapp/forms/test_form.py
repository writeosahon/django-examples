from django import forms

class TestForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=250, required=True, 
                strip=True, label="Your Name ", help_text="enter your name")
    
    age = forms.IntegerField(max_value=999999999999999, min_value=18, label="your age", 
                help_text="provide your age", required=True, initial = 18)

    registration_date = forms.DateField(label="Registration Date", required=True)

    i_agree = forms.BooleanField(label="I Agree", required=True, initial="True", 
                help_text="you must accept our terms to proceed")

from django import forms


class ContactForm(forms.Form):
    template_name = 'projects/form_snippet.html'
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))

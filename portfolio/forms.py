from django import forms

from portfolio.models import Comentario


class ComentarioForm(forms.Form):
    nome = forms.CharField(max_length=50)
    comentario = forms.CharField(widget=forms.Textarea())


class ComentarioModelForm(forms.ModelForm):
    class Meta:
        model = Comentario
        exclude = ['projeto']

from django.forms import ModelForm

from .models import KeySearch


# class GetLinkForm(ModelForm):
#     class Meta:
#         model = GetLink
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(GetLinkForm, self).__init__(*args, **kwargs)
#
#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control mt-3'})
#

class KeySearchForm(ModelForm):
    class Meta:
        model = KeySearch
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(KeySearchForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'placeholder': 'Search...'})

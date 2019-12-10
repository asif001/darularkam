from django import forms


class NoticeForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Write title',
        widget=forms.TextInput(),
    )
    details = forms.CharField(
        max_length=2000,
        label='Write details',
        widget=forms.Textarea(
            attrs={
                'rows': '40',
            }
        ),
    )

    def clean(self):
        cleaned_data = super(NoticeForm, self).clean()
        title = cleaned_data.get('title')
        details = cleaned_data.get('details')
        if not title and not details:
            raise forms.ValidationError('You have to write something!')

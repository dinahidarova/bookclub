from django import forms
from .models import Review, BookRequest


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, f"{i} ★") for i in range(1, 6)],
        widget=forms.RadioSelect,
        label="Оценка"
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Ваш отзыв...'}),
        }


class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = []
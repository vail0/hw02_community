from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
    
    # Метод-валидатор для поля text
    def clean_subject(self):
        data = self.cleaned_data['text']

        # Если пользователь не поблагодарил администратора - считаем это ошибкой
        if data == '':
            raise forms.ValidationError('Поле пустое')

        # Метод-валидатор обязательно должен вернуть очищенные данные, 
        # даже если не изменил их
        return data 
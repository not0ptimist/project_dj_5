## Уточнение по Forms
### Файл с уточняющими ссылками, на моменты из-за которых возникали вопросы 


```
https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserCreationForm
https://docs.djangoproject.com/en/4.0/ref/forms/widgets/#module-django.forms.widgets
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    ...
    
```
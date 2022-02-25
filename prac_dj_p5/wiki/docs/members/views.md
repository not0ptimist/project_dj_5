## Уточнение по Views
### Файл с уточняющими ссылками, на моменты из-за которых возникали вопросы 


```
https://docs.djangoproject.com/en/4.0/topics/auth/
from django.contrib.auth import authenticate, login, logout
...

def login_user(request):
# https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in
    if request.method == 'POST':
    ...
    
```

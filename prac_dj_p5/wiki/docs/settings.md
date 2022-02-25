# Настройка

## DOTENV

С помощья dotenv был убран секретный ключ:  
- создан файл .env, в корневой директории, где находится manage.py  
- в файл settings.py, импортированны, и прописаны пути  
- замена секретных настроек на ссылки на этот файл  

```
import os
from pathlib import Path
from dotenv import load_dotenv

# Loading ENV
env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

```
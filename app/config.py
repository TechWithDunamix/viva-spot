from nexios import MakeConfig
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv,dotenv_values
import os 



BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)
app_config = MakeConfig({
  
    "cors" : {
        "allow_origins" : ["*"]
    },
    **dotenv_values(dotenv_path=dotenv_path)
})


TEMPLATE_DIR =  Path(__file__).resolve().parent.parent / "templates"

template_loader = FileSystemLoader(searchpath=TEMPLATE_DIR)
jinja_env = Environment(loader=template_loader)




db_config =  {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': os.getenv("DB_HOST"),
                'port': os.getenv("DB_PORT"),
                'user': os.getenv("DB_USER"),
                'password': os.getenv("DB_PASSWORD"),
                'database':os.getenv("DB_NAME"),
            }
        }
    },
    "apps": {
        "models": {
            "models": ["app.models","aerich.models"],
            "default_connection": "default",
        }
    }
}


print(db_config)
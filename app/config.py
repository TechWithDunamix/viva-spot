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
                'host': os.getenv("db_host"),
                'port': os.getenv("db_port"),
                'user': os.getenv("db_user"),
                'password': os.getenv("db_password"),
                'database': os.getenv("db_name"),
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

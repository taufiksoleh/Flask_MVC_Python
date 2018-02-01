import os
from flask import Flask

project_root = os.path.dirname(__name__)
template_path = os.path.join(project_root)
app = Flask(__name__,template_folder=template_path)

from app import models
from app import controllers
from flask import Flask
from apps.main.package import main
from utils.devtools import launch

# Run Start-up Scripts
launch()

# Create Main Application
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(main, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)

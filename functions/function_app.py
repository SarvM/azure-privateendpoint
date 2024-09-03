import azure.functions as func
import logging
from blueprints.bp_sample import app_sample
from blueprints.fetch_azure_table import app_fetch_aztables

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

app.register_blueprint(app_sample)
app.register_blueprint(app_fetch_aztables)
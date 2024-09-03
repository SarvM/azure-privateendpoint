from azure.functions import HttpRequest, HttpResponse
import azure.functions as func
import logging, requests

app_sample = func.Blueprint()

@app_sample.route(route="sample", methods=["GET"])
def sample(req: HttpRequest) -> HttpResponse:
    try:
        # Use an external service to fetch the public IP address
        response = requests.get('https://api.ipify.org?format=json')
        public_ip = response.json().get('ip')
    except Exception as e:
        logging.error(f'Error fetching IP address: {e}')
        return func.HttpResponse(f'Error fetching IP address: {e}', status_code=500)
    
    return func.HttpResponse(f'Outbound IP Address: {public_ip}', status_code=200)

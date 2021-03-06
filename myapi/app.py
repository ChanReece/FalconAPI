"""
This is where you define your application
by associated resource objects to their endpoints
"""
import falcon
from resource_healthcheck import HealthResource
from wsgiref.simple_server import make_server

# This creates the WSGI application which understands HTTP
app = falcon.API()

# Instantiate the server resource and associate it to an endpoint
healthcheck_resource = HealthResource()
app.add_route('/v1/healthchecks/ping', healthcheck_resource)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        # Serve until process is killed
        httpd.serve_forever()

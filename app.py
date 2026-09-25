import os
import requests
from flask import Flask, request, Response
app = Flask(__name__)
SERVICES = {name: os.environ.get(name.upper() + '_URL', 'http://' + name + ':5000') for name in ['identity', 'orders', 'files', 'fetch', 'templates', 'jobs', 'archives', 'redirects', 'search']}
@app.route('/api/<service>/<path:path>', methods=['GET', 'POST'])
def proxy(service, path):
    if service not in SERVICES or service == 'identity':
        return 'Not found', 404
    bearer = request.headers.get('Authorization', '')
    if not bearer.startswith('Bearer '):
        return 'Unauthorized', 401
    identity = requests.post(SERVICES['identity'] + '/verify', json={'token': bearer[7:]}, timeout=5)
    if identity.status_code != 200:
        return 'Unauthorized', 401
    principal = identity.json()
    downstream = requests.request(request.method, SERVICES[service] + '/' + path,
        params=request.args, data=request.get_data(), timeout=10, allow_redirects=False,
        headers={'X-User-Id': principal['user_id'], 'Content-Type': request.content_type or 'application/octet-stream'})
    headers = {k: v for k, v in downstream.headers.items() if k.lower() in ('content-type', 'location')}
    return Response(downstream.content, status=downstream.status_code, headers=headers)

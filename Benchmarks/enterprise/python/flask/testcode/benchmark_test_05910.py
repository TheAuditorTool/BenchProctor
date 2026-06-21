# SPDX-License-Identifier: Apache-2.0
import os
import requests
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest05910():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    request_state['last_input'] = api_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
import re
import requests
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest11210():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    request_state['last_input'] = api_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

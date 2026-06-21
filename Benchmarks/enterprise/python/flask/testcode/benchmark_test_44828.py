# SPDX-License-Identifier: Apache-2.0
import os
import json
import requests
from flask import jsonify


def BenchmarkTest44828():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = json.loads(api_value).get('value', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

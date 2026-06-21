# SPDX-License-Identifier: Apache-2.0
import requests
import yaml
from flask import jsonify


def BenchmarkTest33179():
    secret_value = 'app_display_name'
    data = secret_value if secret_value else 'default'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})

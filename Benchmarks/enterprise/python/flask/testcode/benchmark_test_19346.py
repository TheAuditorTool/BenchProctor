# SPDX-License-Identifier: Apache-2.0
import requests
import yaml
from flask import jsonify


def BenchmarkTest19346():
    secret_value = 'default_setting_value'
    data = '%s' % str(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})

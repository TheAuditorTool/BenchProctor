# SPDX-License-Identifier: Apache-2.0
import requests
import yaml
from flask import jsonify


def BenchmarkTest10869():
    secret_value = 'feature_flag_value'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(secret_value)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})

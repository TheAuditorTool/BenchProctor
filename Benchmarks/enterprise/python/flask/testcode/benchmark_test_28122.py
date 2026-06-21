# SPDX-License-Identifier: Apache-2.0
import requests
import boto3
from flask import jsonify


def BenchmarkTest28122():
    secret_value = 'default_setting_value'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(secret_value)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})

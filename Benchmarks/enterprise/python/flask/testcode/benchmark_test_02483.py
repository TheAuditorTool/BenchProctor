# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import yaml
from flask import jsonify
from app_runtime import ssm_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02483():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    ctx = RequestContext(ssm_value)
    data = ctx.payload
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})

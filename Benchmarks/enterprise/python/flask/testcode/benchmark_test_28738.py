# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import yaml
from flask import jsonify
from app_runtime import ssm_client


def BenchmarkTest28738():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    parts = []
    for token in str(ssm_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})

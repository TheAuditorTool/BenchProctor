# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import json
from app_runtime import ssm_client


def BenchmarkTest21346():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    try:
        data = json.loads(ssm_value).get('value', ssm_value)
    except (json.JSONDecodeError, AttributeError):
        data = ssm_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})

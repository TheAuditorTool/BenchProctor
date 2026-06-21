# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from app_runtime import ssm_client


request_state: dict[str, str] = {}

def BenchmarkTest76077():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    request_state['last_input'] = ssm_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})

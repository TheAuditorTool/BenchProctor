# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from dataclasses import dataclass
from flask import jsonify
from app_runtime import ssm_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest02945():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data = FormData(payload=ssm_value).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})

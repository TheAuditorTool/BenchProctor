# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from types import SimpleNamespace
from app_runtime import ssm_client


def BenchmarkTest26936():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    ns = SimpleNamespace(payload=ssm_value)
    data = getattr(ns, 'payload')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest02854():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest70980():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest05062():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

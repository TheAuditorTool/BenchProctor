# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest60500():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

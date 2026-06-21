# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest21044():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})

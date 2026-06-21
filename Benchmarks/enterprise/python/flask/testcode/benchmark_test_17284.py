# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest17284():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})

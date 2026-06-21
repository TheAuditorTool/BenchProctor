# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest26575(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})

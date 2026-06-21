# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from flask import session


@dataclass
class FormData:
    payload: str

def BenchmarkTest50635(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from flask import session


@dataclass
class FormData:
    payload: str

def BenchmarkTest30335():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500

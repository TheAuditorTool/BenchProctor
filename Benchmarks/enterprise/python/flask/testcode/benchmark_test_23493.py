# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest23493():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200

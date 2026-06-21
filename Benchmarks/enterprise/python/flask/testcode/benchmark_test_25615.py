# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest25615():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})

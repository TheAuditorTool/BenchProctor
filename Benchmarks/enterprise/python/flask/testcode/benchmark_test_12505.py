# SPDX-License-Identifier: Apache-2.0
import random
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest12505():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200

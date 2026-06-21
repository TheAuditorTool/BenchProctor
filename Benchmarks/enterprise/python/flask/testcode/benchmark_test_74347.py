# SPDX-License-Identifier: Apache-2.0
import random
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest74347():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200

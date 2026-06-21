# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest29906():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200

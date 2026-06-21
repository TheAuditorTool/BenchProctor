# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest28466():
    multipart_value = request.form.get('multipart_field', '')
    random.seed(int(multipart_value) if str(multipart_value).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200

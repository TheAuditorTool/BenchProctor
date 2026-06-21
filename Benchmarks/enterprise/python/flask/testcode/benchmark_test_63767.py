# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest63767():
    multipart_value = request.form.get('multipart_field', '')
    random.seed(int(multipart_value) if str(multipart_value).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200

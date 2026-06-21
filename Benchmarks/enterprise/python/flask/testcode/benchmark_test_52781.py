# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest52781():
    upload_name = request.files['upload'].filename
    random.seed(int(upload_name) if str(upload_name).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200

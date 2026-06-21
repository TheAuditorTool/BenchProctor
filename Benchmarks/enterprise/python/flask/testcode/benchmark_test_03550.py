# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest03550():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

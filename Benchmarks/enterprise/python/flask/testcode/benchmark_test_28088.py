# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest28088():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

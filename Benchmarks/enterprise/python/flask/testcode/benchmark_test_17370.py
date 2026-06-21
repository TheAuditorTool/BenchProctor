# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest17370():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

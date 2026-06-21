# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest04546():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})

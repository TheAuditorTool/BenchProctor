# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest54871():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})

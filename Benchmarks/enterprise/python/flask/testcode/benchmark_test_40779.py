# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest40779():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    os.seteuid(65534)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest33188():
    multipart_value = request.form.get('multipart_field', '')
    os.remove(str(multipart_value))
    return jsonify({"result": "success"})

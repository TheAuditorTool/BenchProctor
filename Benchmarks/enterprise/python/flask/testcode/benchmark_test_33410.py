# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest33410():
    multipart_value = request.form.get('multipart_field', '')
    data = to_text(multipart_value)
    os.remove(str(data))
    return jsonify({"result": "success"})

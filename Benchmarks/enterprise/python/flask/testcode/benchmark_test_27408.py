# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest27408():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    os.remove(str(data))
    return jsonify({"result": "success"})

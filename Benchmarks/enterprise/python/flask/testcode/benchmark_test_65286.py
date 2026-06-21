# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest65286():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    os.remove(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest72001():
    multipart_value = request.form.get('multipart_field', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(multipart_value)).read()
    return jsonify({"result": "success"})

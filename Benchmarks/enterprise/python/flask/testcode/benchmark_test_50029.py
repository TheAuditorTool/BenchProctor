# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import urllib.request


def BenchmarkTest50029():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})

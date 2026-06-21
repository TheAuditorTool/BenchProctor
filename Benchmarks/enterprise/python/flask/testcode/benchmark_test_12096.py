# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def normalise_input(value):
    return value.strip()

def BenchmarkTest12096():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})

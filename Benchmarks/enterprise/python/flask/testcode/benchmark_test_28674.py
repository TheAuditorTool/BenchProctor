# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest28674():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})

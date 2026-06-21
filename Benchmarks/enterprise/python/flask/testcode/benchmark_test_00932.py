# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import json


def BenchmarkTest00932():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    session['data'] = str(data)
    return jsonify({"result": "success"})

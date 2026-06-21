# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import json


def BenchmarkTest78520(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp

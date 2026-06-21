# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import json


def BenchmarkTest31653():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp

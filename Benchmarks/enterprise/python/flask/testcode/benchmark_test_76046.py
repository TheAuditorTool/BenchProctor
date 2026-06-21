# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import json


def BenchmarkTest76046():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    session['data'] = str(data)
    return jsonify({"result": "success"})

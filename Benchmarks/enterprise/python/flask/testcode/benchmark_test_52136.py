# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import os


def BenchmarkTest52136():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

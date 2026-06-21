# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import json


def BenchmarkTest66523():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

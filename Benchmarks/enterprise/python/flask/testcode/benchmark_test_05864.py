# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
import subprocess


def BenchmarkTest05864():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

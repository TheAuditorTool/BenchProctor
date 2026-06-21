# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest44470():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

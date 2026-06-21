# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import request, jsonify
import json


def BenchmarkTest42186():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest00002():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    yaml.safe_load(data)
    return jsonify({"result": "success"})

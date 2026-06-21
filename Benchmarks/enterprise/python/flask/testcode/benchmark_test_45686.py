# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
import defusedxml.ElementTree


def BenchmarkTest45686(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})

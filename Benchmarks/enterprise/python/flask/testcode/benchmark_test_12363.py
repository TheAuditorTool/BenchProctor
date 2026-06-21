# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest12363():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})

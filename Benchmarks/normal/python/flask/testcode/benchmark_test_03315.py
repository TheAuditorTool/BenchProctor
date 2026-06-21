# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest03315():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})

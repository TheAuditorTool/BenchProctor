# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest13873():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})

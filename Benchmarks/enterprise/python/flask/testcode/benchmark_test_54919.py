# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest54919():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    def _primary():
        _resp = requests.get(str(data))
        exec(_resp.text)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})

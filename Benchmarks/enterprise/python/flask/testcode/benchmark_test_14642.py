# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest14642():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})

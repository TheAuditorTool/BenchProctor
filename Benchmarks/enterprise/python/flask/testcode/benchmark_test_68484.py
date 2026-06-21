# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest68484():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})

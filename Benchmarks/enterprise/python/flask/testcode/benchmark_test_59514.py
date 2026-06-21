# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest59514():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    requests.get(str(data))
    return jsonify({"result": "success"})

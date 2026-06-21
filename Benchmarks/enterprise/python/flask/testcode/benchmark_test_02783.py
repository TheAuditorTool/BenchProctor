# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest02783():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    json.loads(data)
    return jsonify({"result": "success"})

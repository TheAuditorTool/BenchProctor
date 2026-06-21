# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest34840():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    json.loads(data)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest58394():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    json.loads(data)
    return jsonify({"result": "success"})

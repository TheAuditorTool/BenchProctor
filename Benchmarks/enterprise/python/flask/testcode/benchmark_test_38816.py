# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38816():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})

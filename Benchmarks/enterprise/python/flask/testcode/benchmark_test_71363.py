# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest71363():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    os.remove(str(data))
    return jsonify({"result": "success"})

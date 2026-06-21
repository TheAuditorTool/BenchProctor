# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest22952():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})

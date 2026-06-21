# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest24503():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    os.remove(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05441():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest78681():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})

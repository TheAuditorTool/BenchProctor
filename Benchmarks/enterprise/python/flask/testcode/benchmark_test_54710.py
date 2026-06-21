# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest54710():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})

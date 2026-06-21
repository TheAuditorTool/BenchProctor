# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest06897():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

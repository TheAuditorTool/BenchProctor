# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest76785():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

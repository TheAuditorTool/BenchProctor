# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import socket


def ensure_str(value):
    return str(value)

def BenchmarkTest72993():
    user_id = request.args.get('id', '')
    data = ensure_str(user_id)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

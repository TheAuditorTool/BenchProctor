# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import socket


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03257():
    user_id = request.args.get('id', '')
    data = default_blank(user_id)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

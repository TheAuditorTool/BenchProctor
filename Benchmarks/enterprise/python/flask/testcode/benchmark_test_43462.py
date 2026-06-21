# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest43462():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

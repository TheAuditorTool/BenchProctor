# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest10093():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

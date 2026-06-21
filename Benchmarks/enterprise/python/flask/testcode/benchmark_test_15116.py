# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest15116():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    s = socket.create_connection((str(forwarded_ip), 80))
    s.close()
    return jsonify({"result": "success"})

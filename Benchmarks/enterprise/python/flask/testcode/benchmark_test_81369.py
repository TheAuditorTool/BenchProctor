# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest81369():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

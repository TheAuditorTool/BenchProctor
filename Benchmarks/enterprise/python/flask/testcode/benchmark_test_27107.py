# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest27107():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    s = socket.create_connection((str(graphql_var), 80))
    s.close()
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import ipaddress
import socket
from flask import request, jsonify


def BenchmarkTest27783():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parsed = urlparse(graphql_var)
    resolved = socket.gethostbyname(parsed.hostname or graphql_var)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = graphql_var.replace(parsed.hostname, resolved) if parsed.hostname else graphql_var
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})

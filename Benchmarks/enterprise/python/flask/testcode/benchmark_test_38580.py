# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import request, jsonify
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest38580():
    xml_value = request.get_data(as_text=True)
    data = RequestPayload(xml_value).value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})

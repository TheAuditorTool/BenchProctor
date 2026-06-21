# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest23668():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})

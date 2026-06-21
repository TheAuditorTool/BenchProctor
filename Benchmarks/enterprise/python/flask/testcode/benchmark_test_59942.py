# SPDX-License-Identifier: Apache-2.0
import os
import requests
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest59942():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    ns = SimpleNamespace(payload=api_value)
    data = getattr(ns, 'payload')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

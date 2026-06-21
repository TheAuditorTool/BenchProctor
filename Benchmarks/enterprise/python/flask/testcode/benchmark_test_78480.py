# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest78480():
    xml_value = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(xml_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})

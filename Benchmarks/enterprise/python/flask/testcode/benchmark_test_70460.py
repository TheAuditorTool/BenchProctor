# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest70460():
    xml_value = request.get_data(as_text=True)
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

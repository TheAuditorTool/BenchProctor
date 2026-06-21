# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest30162():
    upload_name = request.files['upload'].filename
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})

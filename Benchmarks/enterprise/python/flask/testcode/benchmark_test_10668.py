# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest10668():
    upload_name = request.files['upload'].filename
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.seteuid(65534)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01012():
    upload_name = request.files['doc'].filename
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})

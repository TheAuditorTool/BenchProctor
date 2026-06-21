# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77752():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

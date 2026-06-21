# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12408():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})

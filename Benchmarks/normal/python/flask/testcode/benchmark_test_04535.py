# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04535():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})

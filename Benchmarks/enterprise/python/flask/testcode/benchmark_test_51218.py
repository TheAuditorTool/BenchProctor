# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51218():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})

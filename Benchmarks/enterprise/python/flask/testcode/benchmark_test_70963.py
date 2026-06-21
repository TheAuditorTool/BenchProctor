# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest70963():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    session['data'] = str(processed)
    return jsonify({"result": "success"})

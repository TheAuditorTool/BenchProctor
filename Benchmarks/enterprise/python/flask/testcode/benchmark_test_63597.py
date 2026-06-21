# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest63597():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

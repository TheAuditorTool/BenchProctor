# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest64733():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest12306():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

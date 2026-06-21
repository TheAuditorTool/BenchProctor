# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest72867():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

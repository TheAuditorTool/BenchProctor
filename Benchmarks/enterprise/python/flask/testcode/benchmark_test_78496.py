# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def BenchmarkTest78496():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

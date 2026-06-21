# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest61498():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

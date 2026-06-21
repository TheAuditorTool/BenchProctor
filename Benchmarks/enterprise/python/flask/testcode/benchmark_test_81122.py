# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def BenchmarkTest81122():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})

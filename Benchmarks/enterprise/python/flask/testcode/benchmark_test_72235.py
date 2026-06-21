# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest72235():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})

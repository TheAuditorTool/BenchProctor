# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify


def BenchmarkTest72756():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')

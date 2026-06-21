# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify


def BenchmarkTest07216():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')

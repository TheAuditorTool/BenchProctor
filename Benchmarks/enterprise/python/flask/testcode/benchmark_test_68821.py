# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify


def BenchmarkTest68821():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')

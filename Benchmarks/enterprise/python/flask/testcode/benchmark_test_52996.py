# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import os


def BenchmarkTest52996():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200

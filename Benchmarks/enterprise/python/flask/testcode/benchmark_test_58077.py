# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest58077():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200

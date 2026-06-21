# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest34245(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200

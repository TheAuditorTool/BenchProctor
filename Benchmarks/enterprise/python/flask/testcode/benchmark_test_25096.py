# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest25096(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}

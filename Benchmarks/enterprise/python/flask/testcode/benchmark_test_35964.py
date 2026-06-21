# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import jsonify


def BenchmarkTest35964(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)

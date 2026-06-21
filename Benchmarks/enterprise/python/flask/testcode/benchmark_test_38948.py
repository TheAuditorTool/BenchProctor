# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest38948(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)

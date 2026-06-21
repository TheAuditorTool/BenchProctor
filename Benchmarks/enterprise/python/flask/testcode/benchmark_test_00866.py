# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest00866(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)

# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify


def BenchmarkTest20497(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<img src="' + str(processed) + '">')

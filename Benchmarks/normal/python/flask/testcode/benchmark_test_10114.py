# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10114(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<img src="' + str(processed) + '">')

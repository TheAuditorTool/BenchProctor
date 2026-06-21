# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest22972():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

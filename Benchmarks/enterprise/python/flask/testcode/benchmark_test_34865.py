# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest34865():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

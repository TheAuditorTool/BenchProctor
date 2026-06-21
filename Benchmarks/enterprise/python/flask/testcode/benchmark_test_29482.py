# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest29482():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

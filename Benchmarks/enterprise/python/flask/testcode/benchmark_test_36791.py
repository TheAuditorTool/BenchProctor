# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest36791():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

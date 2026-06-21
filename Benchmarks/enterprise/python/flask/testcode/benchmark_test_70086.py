# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest70086():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

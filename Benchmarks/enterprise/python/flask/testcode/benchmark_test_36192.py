# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest36192():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest05177():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

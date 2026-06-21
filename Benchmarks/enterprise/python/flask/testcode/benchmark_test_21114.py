# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest21114():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

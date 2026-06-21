# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest43812():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

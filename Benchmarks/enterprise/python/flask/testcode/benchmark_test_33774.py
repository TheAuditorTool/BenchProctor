# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest33774():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

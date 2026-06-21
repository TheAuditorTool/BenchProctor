# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest37645():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest29035():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = f'{profile_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

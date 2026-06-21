# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest07990():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = relay_value(profile_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

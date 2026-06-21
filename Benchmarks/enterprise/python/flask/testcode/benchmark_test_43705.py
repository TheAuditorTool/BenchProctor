# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest43705():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(profile_value))
    return jsonify({"result": "success"})

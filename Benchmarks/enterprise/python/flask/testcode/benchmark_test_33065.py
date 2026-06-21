# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest33065():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = (lambda v: v.strip())(profile_value)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest77162():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = []
    for token in str(profile_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

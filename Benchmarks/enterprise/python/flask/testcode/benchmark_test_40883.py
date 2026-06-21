# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest40883():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return jsonify({"result": "success"})

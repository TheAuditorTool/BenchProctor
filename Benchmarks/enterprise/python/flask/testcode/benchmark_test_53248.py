# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest53248():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})

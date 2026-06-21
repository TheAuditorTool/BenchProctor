# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest10405():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = json.loads(profile_value).get('value', profile_value)
    except (json.JSONDecodeError, AttributeError):
        data = profile_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp

# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from app_runtime import db


def BenchmarkTest60249():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = str(profile_value).split(',')
    data = ','.join(parts)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp

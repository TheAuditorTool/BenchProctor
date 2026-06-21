# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest76003():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(profile_value)
    data = collected
    processed = re.sub(r'\d+', '****', str(data))
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp

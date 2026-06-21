# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01851():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    reader = make_reader(profile_value)
    data = reader()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp

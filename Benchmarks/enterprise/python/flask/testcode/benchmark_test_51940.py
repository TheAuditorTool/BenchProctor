# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest51940():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200

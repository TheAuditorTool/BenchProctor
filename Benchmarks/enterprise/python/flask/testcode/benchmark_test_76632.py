# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest76632():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ns = SimpleNamespace(payload=profile_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content

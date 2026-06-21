# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest36681():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<script src="' + str(processed) + '"></script>', 200, {'Content-Type': 'text/html'}

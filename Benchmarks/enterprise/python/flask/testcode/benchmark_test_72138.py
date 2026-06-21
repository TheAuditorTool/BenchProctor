# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest72138():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})

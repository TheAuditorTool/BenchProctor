# SPDX-License-Identifier: Apache-2.0
import json
from flask import Flask, jsonify
import os
import redis
import importlib


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))
def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00286", methods=["POST"])
def BenchmarkTest00286():
    redis_value = redis_client.get('user_data')
    data = redis_value.decode('utf-8', 'ignore') if isinstance(redis_value, bytes) else redis_value
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(data))
    return jsonify({'parsed': str(parsed)}), 200

# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Flask, jsonify
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00096", methods=["POST"])
def BenchmarkTest00096():
    redis_value = redis_client.get('user_data')
    data = '{}'.format(redis_value)
    parsed = yaml.safe_load(data)
    return jsonify({'parsed': str(parsed)}), 200

# SPDX-License-Identifier: Apache-2.0
import requests
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


@app.route("/BenchmarkTest00210", methods=["POST"])
def BenchmarkTest00210():
    redis_value = redis_client.get('user_data')
    if redis_value:
        data = redis_value
    else:
        data = ''
    requests.get(str(data))
    return jsonify({"result": "success"})

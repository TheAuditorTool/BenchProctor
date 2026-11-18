# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import base64
import pickle
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


@app.route("/BenchmarkTest00072", methods=["POST"])
def BenchmarkTest00072():
    redis_value = redis_client.get('user_data')
    data = str(redis_value).replace('\x00', '')
    pickle.loads(base64.b64decode(data))
    return jsonify({"result": "success"})

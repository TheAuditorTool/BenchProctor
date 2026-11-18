# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import socket
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


@app.route("/BenchmarkTest00165", methods=["POST"])
def BenchmarkTest00165():
    redis_value = redis_client.get('user_data')
    data = f'{redis_value!s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})

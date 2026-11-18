# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Flask, jsonify
import socket
import re
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


@app.route("/BenchmarkTest00645", methods=["POST"])
def BenchmarkTest00645():
    redis_value = redis_client.get('user_data')
    kind = 'json' if str(redis_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(redis_value).strip()
        case _:
            data = str(redis_value)
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})

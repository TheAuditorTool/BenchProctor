# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Flask, jsonify
import socket
import urllib.parse
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


@app.route("/BenchmarkTest00046", methods=["POST"])
def BenchmarkTest00046():
    redis_value = redis_client.get('user_data')
    parts = []
    for token in str(redis_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((urllib.parse.urlparse(str(target_url)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})

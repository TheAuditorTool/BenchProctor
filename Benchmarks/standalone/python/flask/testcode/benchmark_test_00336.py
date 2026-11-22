# SPDX-License-Identifier: Apache-2.0
from flask import Flask, abort
from flask import redirect
from urllib.parse import urlparse
from flask import jsonify
import re
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00336", methods=["POST"])
def BenchmarkTest00336():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    abort(redirect(str(target_url)))

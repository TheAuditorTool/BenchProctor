# SPDX-License-Identifier: Apache-2.0
from flask import Flask, Response
from flask import render_template_string
from app_runtime import db
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00258", methods=["POST"])
def BenchmarkTest00258():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    resp = Response(mimetype='text/html')
    resp.stream.write(render_template_string('<div>{{ value }}</div>', value=str(comment_value)))
    return resp

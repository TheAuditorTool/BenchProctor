# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00039", methods=["POST"])
def BenchmarkTest00039():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '%s' % (profile_value,)
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return jsonify({"result": "success"})

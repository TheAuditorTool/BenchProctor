# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import request, jsonify
from pydantic import Field, ValidationError, create_model


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00296", methods=["POST"])
def BenchmarkTest00296():
    multipart_value = request.form.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import ldap
import jsonschema
from flask import Flask, request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00142", methods=["POST"])
def BenchmarkTest00142():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = RequestPayload(json_value).value
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.#%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(processed) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return jsonify({"result": "success"})

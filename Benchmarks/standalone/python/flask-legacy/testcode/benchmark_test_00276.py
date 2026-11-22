# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import Flask, request, jsonify
import os


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00276", methods=["POST"])
def BenchmarkTest00276():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(data) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return jsonify({"result": "success"})

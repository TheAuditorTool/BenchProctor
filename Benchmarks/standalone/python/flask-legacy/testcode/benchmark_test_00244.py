# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00244", methods=["POST"])
def BenchmarkTest00244():
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % (env_value,)
    _des_key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()[:8]
    ciphertext = DES.new(_des_key, DES.MODE_ECB).encrypt(pad(str(data).encode(), 8))
    return jsonify({'length': len(ciphertext)}), 200

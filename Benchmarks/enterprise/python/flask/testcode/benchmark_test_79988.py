# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest79988():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

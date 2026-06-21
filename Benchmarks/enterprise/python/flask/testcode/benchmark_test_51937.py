# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest51937():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200

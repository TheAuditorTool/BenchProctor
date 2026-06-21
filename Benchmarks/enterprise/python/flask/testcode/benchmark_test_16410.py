# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import jsonify
import os
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest16410():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200

# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest01887():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

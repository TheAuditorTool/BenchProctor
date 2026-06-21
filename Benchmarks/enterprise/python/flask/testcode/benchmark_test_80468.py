# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from cryptography.fernet import Fernet
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest80468():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ns = SimpleNamespace(payload=profile_value)
    data = getattr(ns, 'payload')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp

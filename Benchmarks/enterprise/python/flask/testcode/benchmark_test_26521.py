# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest26521():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

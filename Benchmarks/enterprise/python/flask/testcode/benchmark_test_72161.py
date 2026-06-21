# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest72161():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67068():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

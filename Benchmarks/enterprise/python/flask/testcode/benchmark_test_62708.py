# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62708():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

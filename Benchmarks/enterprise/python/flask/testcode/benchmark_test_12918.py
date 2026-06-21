# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12918():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

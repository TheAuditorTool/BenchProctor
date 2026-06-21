# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16742():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46079():
    xml_value = request.get_data(as_text=True)
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(xml_value).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

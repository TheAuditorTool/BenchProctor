# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest44852(path_param):
    path_value = path_param
    processed = 'true' if str(path_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

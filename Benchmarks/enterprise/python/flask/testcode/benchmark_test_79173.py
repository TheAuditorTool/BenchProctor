# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79173():
    xml_value = request.get_data(as_text=True)
    allowed_fields = {'name', 'email', 'bio'}
    if str(xml_value).split('=', 1)[0] not in allowed_fields:
        return jsonify({'error': 'field not allowed'}), 400
    processed = xml_value
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return jsonify({'is_admin': profile.is_admin}), 200

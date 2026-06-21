# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest64615():
    xml_value = request.get_data(as_text=True)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(xml_value)):
        return jsonify({'error': 'invalid input'}), 400
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

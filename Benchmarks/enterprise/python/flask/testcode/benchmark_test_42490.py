# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest42490():
    user_id = request.args.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(user_id)):
        return jsonify({'error': 'invalid input'}), 400
    processed = user_id
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)

# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest09147():
    upload_name = request.files['upload'].filename
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return jsonify({'error': 'forbidden'}), 400
    processed = upload_name
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)

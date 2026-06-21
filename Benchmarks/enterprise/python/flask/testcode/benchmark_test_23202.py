# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest23202():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73622():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}

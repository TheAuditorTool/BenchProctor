# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05458():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}

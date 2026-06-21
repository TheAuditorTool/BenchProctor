# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest76237():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}

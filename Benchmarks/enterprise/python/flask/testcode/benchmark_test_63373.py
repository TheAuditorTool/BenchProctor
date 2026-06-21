# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest63373():
    origin_value = request.headers.get('Origin', '')
    data = coalesce_blank(origin_value)
    eval(compile("with open('/var/log/app_audit.log', 'a') as fh:\n    fh.write(str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest50370():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    eval(compile("with open('/var/www/html/exports/report.txt', 'w') as fh:\n    fh.write(str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})

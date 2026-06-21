# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest48741():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ns = SimpleNamespace(payload=config_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp

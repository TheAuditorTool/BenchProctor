# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest38052():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(config_value)
    data = collected
    processed = data[:64]
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp

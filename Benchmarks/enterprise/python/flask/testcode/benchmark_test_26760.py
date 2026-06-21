# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest26760():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(config_value), max_age=86400)
    return resp

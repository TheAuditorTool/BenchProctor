# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest47668():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value:.200s}'
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp

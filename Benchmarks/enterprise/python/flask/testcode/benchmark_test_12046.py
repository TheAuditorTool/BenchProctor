# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest12046():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = ' '.join(str(config_value).split())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp

# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest25390():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = FormData(payload=config_value).payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp

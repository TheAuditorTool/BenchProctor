# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest41775():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    kind = 'json' if str(prop_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = prop_value
            data = parsed
        case _:
            data = prop_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})

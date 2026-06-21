# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest11704():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    kind = 'json' if str(yaml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = yaml_value
            data = parsed
        case _:
            data = yaml_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})

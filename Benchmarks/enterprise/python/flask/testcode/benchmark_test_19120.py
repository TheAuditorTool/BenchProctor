# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest19120():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data, _sep, _rest = str(config_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

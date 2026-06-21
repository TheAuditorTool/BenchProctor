# SPDX-License-Identifier: Apache-2.0
import logging
import re
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest55744():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = FormData(payload=yaml_value).payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
